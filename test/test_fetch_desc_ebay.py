"""
Copyright (c) 2021 Anshul Patel
This code is licensed under MIT license (see LICENSE.MD for details)

@author: cheapBuy
"""

import sys
sys.path.append('../')
from FetchDescription import FetchDescription

def test_fetch_description_ebay():
    link = "https://www.ebay.com/itm/274922036305?epid=25014370331&hash=item4002a15c51:g:v8UAAOSwsv1hKB7z"
    fd = FetchDescription(link)
    assert fd.fetch_desc_ebay() == "3x Brita Longlast Water Filter Replacement  - NEW Sealed"

