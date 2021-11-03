# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 15:33:22 2021

@author: Rohan Shah
"""

from bs4 import BeautifulSoup
from threading import Thread
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class WebScrapper_Amazon(Thread):
    
    def __init__(self,description):
        self.driver = self.get_driver()
        self.description = description
        self.result = {}
        super(WebScrapper_Amazon,self).__init__()
    
    def run(self):
        try:
            results = self.scrap_amazon()
            if len(results) == 0:
                print('Amazon_results empty')
                self.result = {}
            else:
                item=results[0]
                atag = item.h2.a
                self.result['description'] = atag.text.strip()
                self.result['url'] = 'https://www.amazon.com'+atag.get('href')
                price_parent = item.find('span', 'a-price')
                self.result['price'] = price_parent.find('span', 'a-offscreen').text
                self.result['site'] = 'amazon'
        except:
            print('Amazon_results exception')
            self.result={}

    def get_driver(self):
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=options, executable_path=ChromeDriverManager().install())
        return driver
    
    def get_url_amazon(self):
        try:
            template = 'https://www.amazon.com'+'/s?k={}&ref=nb_sb_ss_ts-doa-p_3_5'
            search_term = self.description.replace(' ','+')
            template = template.format(search_term)
        except:
            template = ''
        return template

    def scrap_amazon(self):
        results=[]
        try:
            url = self.get_url_amazon()
            self.driver.get(url)
            soup = BeautifulSoup(self.driver.page_source, 'html.parser')
            results = soup.find_all('div',{'data-component-type': 's-search-result'})
        except:
            results = []
        return results



