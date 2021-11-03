# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 15:34:50 2021

@author: Rohan Shah
"""

from bs4 import BeautifulSoup
from threading import Thread

class WebScrapper_Bjs(Thread):
    
    def __init__(self,driver,description):
        self.driver = driver
        if len(description)<5:
            self.description = description
        else:
            self.description = ' '.join(description.split()[:5])
        self.result = None
        super(WebScrapper_Bjs,self).__init__()
    
    def run(self):
        try:
            results = self.scrap_bjs()
            self.result={}
            if len(results) == 0:
                self.result={}
            else:
                item=results[1]
                atag = item.find("a",{"class":"product-link mt-xl-3 mt-xs-3 mt-md-0 mt-3"})
                self.result['description'] = (atag.find("h2",{"class":"product-title no-select d-none"})).text
                self.result['url'] = "www.bjs.com" + str(atag.get('href'))
                self.result['price'] = item.find("div",{"class":"display-price"}).find('span',{'class':'price'}).text
                self.result['site'] = 'bjs'
        except:
            self.result={}
    
    def get_url_bjs(self):
        template = "https://www.bjs.com"+"/search/{}"
        search_term = self.description.replace(' ','+')
        return template.format(search_term)

    def scrap_bjs(self):
        url = self.get_url_bjs()
        self.driver.get(url)
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        results = soup.find_all('div',{'class': 'products-list'})
        return results

        

