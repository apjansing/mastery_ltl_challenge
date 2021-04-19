import json
import datetime
from flask import Flask, request
import requests
import os
from MongoOps import MongoOps


app = Flask(__name__)
mongo_ops = MongoOps()

def check_schema(schema, data):
    '''
    schema: Schema dict with dtypes in values.
    data: Sample input dictionary to be validated.
    '''
    s_keys = set(schema.keys())
    d_keys = set(data.keys())
    if len(s_keys ^ d_keys) > 0: # makes sure the symmetric difference size is 0. i.e. the sets are the same
        return False
    return sum([ isinstance(item[1], schema[item[0]]) for item in data.items() ]) == len(data)



@app.route('/make_shipment', methods=['POST'])
def make_shipment():
    """
    shipment = { 
        ID: string,
        Weight: integer,
        Origin_Latitude: float,
        Origin_Longitude: float,
        Destination_Latitude: float,
        Destination_Longitude: float
    }
    """
    shipment = json.loads(request.data)
    schema = {
            'ID': str,
            'Weight': int,
            'Origin_Latitude': float,
            'Origin_Longitude': float,
            'Destination_Latitude': float,
            'Destination_Longitude': float
         }
    valid = check_schema(schema, shipment) 
    if not valid:
        return "INVALID INPUT"
    
    success, insert_results = mongo_ops.insert_shipment(shipment)
    if success:
        return f'''
        
        {shipment} is a valid input.
        Database ID: {insert_results}.

        '''
    return insert_results

@app.route('/make_truck', methods=['POST'])
def make_truck():
    """
    truck = {
        ID: string,
        Capacity: integer,
        Origin_Latitude: float,
        Origin_Longitude: float,
        Destination_Latitude: float,
        Destination_Longitude: float
    }
    """
    truck = json.loads(request.get_data())
    schema = {
        'ID': str,
        'Capacity': int,
        'Origin_Latitude': float,
        'Origin_Longitude': float,
        'Destination_Latitude': float,
        'Destination_Longitude': float
        }
    valid = check_schema(schema, truck) 
    if not valid:
        return "INVALID INPUT"
    
    success, insert_results = mongo_ops.insert_truck(truck)
    if success:
        return f'''
        
        {truck} is a valid input.
        Database ID: {insert_results}.

        '''
    return insert_results

@app.route('/')
@app.route('/<path:p>')
def wikiproxy(p = ''):
    import requests
    url = 'https://apjansing.github.io/mastery_ltl_challenge/{0}'.format(p)
    try:
        r = requests.get(url)
    except Exception as e:
        return "proxy service error: " + str(e), 503
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(r.content, "html.parser")
    return str(soup)

if __name__ == '__main__':
    app.run(host="0.0.0.0")