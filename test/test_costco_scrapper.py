# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 00:11:19 2021

@author: Rohan Shah
"""

import sys
sys.path.append('../')
from WebScrapper_Costco import WebScrapper_Costco

def test_costco_scrapper():
    
    description = 'brita replacement filters%2c 10 pack'
    t = WebScrapper_Costco(description)
    t.start()
    t.join()
    assert t.result == {'description': 'Brita Replacement Filters, 10-pack\n\t\t\t',
     'url': 'https://tinyurl.com/yfznxg8z',
     'price': '$39.99',
     'site': 'costco'}