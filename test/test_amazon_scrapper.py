# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 00:11:19 2021

@author: Rohan Shah
"""

import sys
sys.path.append('../')
from WebScrapper_Amazon import WebScrapper_Amazon

def test_amazon_scrapper():
    
    description = 'Brita 35503 Standard Replacement Filters'
    t = WebScrapper_Amazon(description)
    t.start()
    t.join()
    assert t.result == {'description': 'Sapphire Water Filters compatible with Sapphire, Brita and Pur Pitchers, 6-Pack',
     'url': 'https://tinyurl.com/yjy52tsm',
     'price': '$27.95',
     'site': 'amazon'}