# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 14:41:54 2021

@author: Rohan Shah
"""

import os
import sys
sys.path.append(os.path.abspath('../../../'))
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import FetchDescription
import WebScrapper_Amazon
import WebScrapper_Bjs
#import WebScrapper_Costco
import WebScrapper_Ebay
import WebScrapper_Walmart

class WebScrapper:
    
    def __init__(self,product_link):
        self.product_link = product_link
    
    def get_driver(self):
        options = webdriver.ChromeOptions()
        options.headless = True
        driver = webdriver.Chrome(options=options, executable_path=ChromeDriverManager().install())
        return driver

    def get_description(self):
        if 'walmart' in self.product_link:
            source = 'walmart'
            fd = FetchDescription(source)
            description = fd.fetch_desc_walmart()
        elif 'amazon' in self.product_link:
            source = 'amazon'
            fd = FetchDescription(source)
            description = fd.fetch_desc_amazon()
        elif 'ebay' in self.product_link:
            source = 'ebay'
            fd = FetchDescription(source)
            description = fd.fetch_desc_ebay()
        elif 'costco' in self.product_link:
            source = 'costco'
            fd = FetchDescription(source)
            description = fd.fetch_desc_costco()
        elif 'bjs' in self.product_link:
            source= 'bjs'
            fd = FetchDescription(source)
            description = fd.fetch_desc_bjs()
        else:
            source = 'N/A'
        
        return description
    
    def call_scrapper(self):
        product_description = self.get_description()
        print(product_description)
        
        driver = self.get_driver()
        
        results_amazon = WebScrapper_Amazon(driver,product_description).extract_item_amazon()
        results_walmart = WebScrapper_Walmart(driver,product_description).extract_item_walmart()
        results_ebay = WebScrapper_Ebay(driver,product_description).extract_item_ebay()
        results_costco = 1
        results_bjs = WebScrapper_Bjs(driver,product_description).extract_item_bjs()
        
        return [results_amazon,results_walmart,results_ebay,results_costco,results_bjs]
        