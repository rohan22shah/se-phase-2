# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 23:52:22 2021

@author: Rohan Shah
"""

import sys
sys.path.append('../')
from FetchDescription import FetchDescription

def test_fetch_description_bjs():
    link = "https://www.bjs.com/product/brita-pour-through-pitcher-replacement-filter-10-pk/23578"
    fd = FetchDescription(link)
    assert fd.fetch_desc_bjs() == "brita pour through pitcher replacement filter 10 pk"
    
