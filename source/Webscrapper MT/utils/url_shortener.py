# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 17:08:18 2021

@author: Rohan Shah
"""

from pyshorteners import Shortener 

def shorten_url(url):
    s = Shortener()
    short_url = s.tinyurl.short(url)
    return short_url
