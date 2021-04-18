import json
import datetime
import pandas as pd

from flask import Flask
import requests

import os

app = Flask(__name__)

@app.route('/get_directions/<coordinates>')
def get_directions(coordinates):
    """
    TODO
    """
    return ""

@app.route('/get_geocode/<address>')
def get_geocoded(address):
    """
    TODO
    """
    return ""

@app.route('/')
@app.route('/<path:p>')
def wikiproxy(p = ''):
    import requests
    url = 'https://apjansing.github.io/Open-House-Route-Planner/{0}'.format(p)
    try:
        r = requests.get(url)
    except Exception as e:
        return "proxy service error: " + str(e), 503
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(r.content, "html.parser")
    return str(soup)

if __name__ == '__main__':
    app.run(host="0.0.0.0")