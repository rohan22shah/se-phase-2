# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 15:34:50 2021

@author: Rohan Shah
"""

from bs4 import BeautifulSoup

class WebScrapper_Bjs():
    
    def __init__(self,driver,description):
        self.driver = driver
        self.description = description
    
    def get_url_bjs(self):
        template="https://www.bjs.com"+"/search/{}"
        return template.format(self.description)

    def scrap_bjs(self):
        url = self.get_url_bjs()
        driver=self.driver.get(url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        results = soup.find_all("div",{"class":"each-section"})
        return results

    def extract_item_bjs(self):
        result={}
        results = self.scrap_bjs()
        if len(results) == 0:
          return result 
        item=results[1]
        atag = item.find("a",{"class":"product-link mt-xl-3 mt-xs-3 mt-md-0 mt-3"})
        result['url'] = 'https://www.bjs.com'+atag.get('href')
        result['description'] = item.find("h2",{"class":"product-title no-select d-none"})
        if(result['description']==None):
          result['description']=item.find("h2",{"class":"product-title no-select d-none d-sm-block"}).get_text().strip()
        else:
          result['description']=result['description'].get("title")
        result['description']=result['description'].replace(" | safeHtml","")
        result['price'] = item.find("div",{"class":"price-block no-select"}).get_text().strip().strip('$')
        result['site'] = 'bjs'
        return result

