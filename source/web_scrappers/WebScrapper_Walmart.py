# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 15:34:11 2021

@author: Rohan Shah
"""

from bs4 import BeautifulSoup
from threading import Thread

class WebScrapper_Walmart(Thread):
    
    def __init__(self,driver,description):
        self.driver = driver
        self.description = description
        self.result = {}
        super(WebScrapper_Walmart,self).__init__()
        
    def run(self):
        self.result={}
        try:
            results = self.scrap_walmart()
            if len(results) == 0:
                self.result = {} 
            item=results[0]
            atag = item.find("a",{"class":"absolute w-100 h-100 z-1"})
            self.result['description'] = (atag.find("span",{"class":"w_D1"})).text
            self.result['url'] = atag.get('href')
            parent_price= item.find("div",{"class":"flex flex-wrap justify-start items-center lh-title mb2 mb1-m"})
            self.result['price'] = parent_price.find("div", {"class":"b black f5 mr1 mr2-xl lh-copy f4-l"}).text.strip('$')
            self.result['site'] = 'walmart'
            return self.result
        except:
            self.result = {}
        
    def get_url_walmart(self):
        template = 'https://www.walmart.com/search?q={}'
        search_term = self.description.replace(' ','+')
        return template.format(search_term)

    def scrap_walmart(self):
        url = self.get_url_walmart()
        self.driver.get(url)
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        results = soup.find_all('div',{'class': 'h-100 pb1-xl pr4-xl pv1 ph1'})
        print('results:{}'.format(results))
        return results

