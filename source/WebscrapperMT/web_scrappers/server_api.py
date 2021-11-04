# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 15:28:06 2021

@author: Rohan Shah
"""

import json
from WebScrapper import WebScrapper
from flask import Flask

app = Flask(__name__)

@app.route('/fetch', methods=['GET'])
def execute():
    url = 'https://www.walmart.com/ip/Brita-Longlast-Water-Filter-Replacement-Reduces-Lead-2-Count/128876038'
    ws = WebScrapper(url)
    result = ws.call_scrapper()
    jsonStr = json.dumps(result)
    return jsonStr

app.run()