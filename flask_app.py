import json
import datetime
import pandas as pd
from flask import Flask
import requests
import os
from schema import Schema, And, Use, SchemaError


app = Flask(__name__)

def check_schema(conf_schema, conf):
    try:
        conf_schema.validate(conf)
        return ""
    except SchemaError:
        return SchemaError

@app.route('/make_shipment/<shipment>', methods=['POST'])
def make_shipment(shipment):
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
    conf_schema = Schema({
        'ID': And(Use(str)),
        'Weight': And(Use(int)),
        'Origin_Latitude': And(Use(float)),
        'Origin_Longitude': And(Use(float)),
        'Destination_Latitude': And(Use(float)),
        'Destination_Longitude': And(Use(float))
        })
    schema_validation = check_schema(conf_schema, shipment)
    if schema_validation != None:
        return schema_validation
        
    return ""

@app.route('/make_truck/<truck>', methods=['POST'])
def make_truck(truck):
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
    conf_schema = Schema({
        'ID': And(Use(str)),
        'Capacity': And(Use(int)),
        'Origin_Latitude': And(Use(float)),
        'Origin_Longitude': And(Use(float)),
        'Destination_Latitude': And(Use(float)),
        'Destination_Longitude': And(Use(float))
        })
    schema_validation = check_schema(conf_schema, truck)
    if schema_validation != None:
        return schema_validation
    
    return ""

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