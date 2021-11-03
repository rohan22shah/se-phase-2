# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 15:34:33 2021

@author: Rohan Shah
"""

from bs4 import BeautifulSoup
from threading import Thread

class WebScrapper_Ebay(Thread):
    
    def __init__(self,driver,description):
        self.driver = driver
        self.description = description
        self.result = None
        super(WebScrapper_Ebay,self).__init__()
        
    def run(self):
        self.result={}
        try:
            results = self.scrap_ebay()
            if len(results) == 0:
                self.result = {}
            item=results[0]
            atag = item.find("a",{"class":"s-item__link"})
            self.result['description'] = item.find("h3",{"class":"s-item__title"}).get_text().strip()
            self.result['url'] = atag.get('href')
            self.result['price'] = item.find("span",{"class":"s-item__price"}).get_text().strip().strip('$')
            self.result['site'] = 'ebay'
        except:
            self.result = {}
        
        
    def get_url_ebay(self):
      try:
          template="https://www.ebay.com"+"/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw={}"
          template=template.format(self.description)
      except:
          template = ''
      return template

    def scrap_ebay(self):
        results = []
        try:
            url = self.get_url_ebay()
            self.driver.get(url)
            print(url)
            soup = BeautifulSoup(self.driver.page_source, 'html.parser')
            results = soup.find_all("li",{"class":"s-item s-item__pl-on-bottom s-item--watch-at-corner"})
        except:
            results = []
        return results
