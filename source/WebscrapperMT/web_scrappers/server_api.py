"""
Copyright (c) 2021 Anshul Patel
This code is licensed under MIT license (see LICENSE.MD for details)

@author: cheapBuy
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