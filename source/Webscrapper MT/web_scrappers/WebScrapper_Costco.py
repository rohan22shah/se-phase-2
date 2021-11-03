# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 15:34:40 2021

@author: Rohan Shah
"""

from bs4 import BeautifulSoup
from threading import Thread
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class WebScrapper_Costco(Thread):
    
    def __init__(self,description):
        self.driver = self.get_driver()
        if len(description)<5:
            self.description = description
        else:
            self.description = ' '.join(description.split()[:5])
        self.result = None
        super(WebScrapper_Costco,self).__init__()
        
    def run(self):
        self.result={}
        try:
            results = self.scrap_costco()
            if len(results) == 0:
                print('Costco_results empty')
                self.result={}
            else:                
                item=results[0]
                atag = item.find("span",{"class":"description"}).find('a')
                self.result['description'] = atag.text
                self.result['url'] = atag.get('href')
                self.result['price'] = item.find("div",{"class":"price"}).text.strip()
                self.result['site'] = 'costco'
        except:
            print('Costco_results exception')
            self.result={}
            
    def get_driver(self):
        options = webdriver.ChromeOptions()
        #options.headless = True
        driver = webdriver.Chrome(options=options, executable_path=ChromeDriverManager().install())
        return driver
    
    def get_url_costco(self):
        template = "https://www.costco.com"+"/CatalogSearch?dept=All&keyword={}"
        search_term = self.description.replace(' ','+')
        return template.format(search_term)

    def scrap_costco(self):
        url = self.get_url_costco()
        self.driver.get(url)
        soup = BeautifulSoup(self.driver.page_source,"html.parser")
        results = soup.find_all('div',{'class': 'product-list grid'})
        return results
        

