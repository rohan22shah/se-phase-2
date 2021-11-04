# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 00:11:19 2021

@author: Rohan Shah
"""

import sys
sys.path.append('../')
from WebScrapper_Bjs import WebScrapper_Bjs

def test_bjs_scrapper():
    
    description = 'brita pour through pitcher replacement filter 10 pk'
    t = WebScrapper_Bjs(description)
    t.start()
    t.join()
    assert t.result == {'description': 'Brita Pour-Through Pitcher Replacement Filter, 10 pk.',
     'url': 'https://tinyurl.com/yfgukkgl',
     'price': '$39.99 ',
     'site': 'bjs'}