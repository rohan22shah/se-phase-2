# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 23:52:22 2021

@author: Rohan Shah
"""

import sys
sys.path.append('../')
from FetchDescription import FetchDescription

def test_fetch_description_amazon():
    link = "https://www.amazon.com/Brita-35503-Standard-Replacement-Filters/dp/B00004SU18/ref=sr_1_1_sspa?crid=1JAEDEIU0E97P&dchild=1&keywords=brita+filter&qid=1635998477&sprefix=brita+filte%2Caps%2C146&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExNTY0RlhRSk9KSVcyJmVuY3J5cHRlZElkPUEwMDgzMTU1Mk9WUExKUThERkhIJmVuY3J5cHRlZEFkSWQ9QTA3NDY5MDVLUFlENFVKNkFXRzQmd2lkZ2V0TmFtZT1zcF9hdGYmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl"
    fd = FetchDescription(link)
    assert fd.fetch_desc_amazon() == "Brita 35503 Standard Replacement Filters"
