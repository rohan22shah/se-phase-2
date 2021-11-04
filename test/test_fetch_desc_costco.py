"""
Copyright (c) 2021 Anshul Patel
This code is licensed under MIT license (see LICENSE.MD for details)

@author: cheapBuy
"""

import sys
sys.path.append('../')
from FetchDescription import FetchDescription

def test_fetch_description_costco():
    link = "https://www.costco.com/brita-replacement-filters%2c-10-pack.product.100131571.html"
    fd = FetchDescription(link)
    assert fd.fetch_desc_costco() == "brita replacement filters%2c 10 pack"
    
