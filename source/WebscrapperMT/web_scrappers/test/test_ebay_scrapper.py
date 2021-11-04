# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 00:11:19 2021

@author: Rohan Shah
"""

import sys
sys.path.append('../')
from WebScrapper_Ebay import WebScrapper_Ebay

def test_ebay_scrapper():
    
    description = '3x Brita Longlast Water Filter Replacement  - NEW Sealed'
    t = WebScrapper_Ebay(description)
    t.start()
    t.join()
    assert t.result == {'description': '3x Brita Longlast Water Filter Replacement  - NEW Sealed',
     'url': 'https://tinyurl.com/yg7pognr',
     'price': '$20.00',
     'site': 'ebay'}