"""
Copyright (c) 2021 Anshul Patel
This code is licensed under MIT license (see LICENSE.MD for details)

@author: cheapBuy
"""

import sys
sys.path.append('../')
from FetchDescription import FetchDescription
    
def test_fetch_description_walmart():
    link = "https://www.walmart.com/ip/Brita-Longlast-Water-Filter-Replacement-Reduces-Lead-2-Count/128876038"
    fd = FetchDescription(link)
    assert fd.fetch_desc_walmart() == "Brita Longlast Water Filter Replacement Reduces Lead 2 Count"
    
