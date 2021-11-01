# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 15:34:11 2021

@author: Rohan Shah
"""

from bs4 import BeautifulSoup

class WebScrapper_Walmart():
    
    def __init__(self,driver,description):
        self.driver = driver
        self.description = description
        
    def get_url_walmart(self):
        template = 'https://www.walmart.com/search?q={}'
        search_term = self.description.replace(' ','+')
        return template.format(search_term)

    def scrap_walmart(self):
        url = self.get_url_walmart()
        driver = self.driver.get(url)
        soup = BeautifulSoup(driver.page_source)
        results = soup.find_all('div',{'class': 'flex flex-wrap w-100 flex-grow-0 flex-shrink-0 ph2 pr0-xl pl4-xl mt0-xl mt3'})
        print('results:{}'.format(results))
        return results

    def extract_item_walmart(self):
        result={}
        results = self.scrap_walmart()
        if len(results) == 0:
            return result 
        item=results[0]
        atag = item.find("a",{"class":"absolute w-100 h-100 z-1"})
        result['description'] = atag.find("span",{"class":"w_Cs"}).text
        result['url'] = atag.get('href')
        parent_price= item.find("div",{"class":"flex flex-wrap justify-start items-center lh-title mb2 mb1-m"})
        result['price'] = parent_price.find("div", {"class":"b black f5 mr1 mr2-xl lh-copy f4-l"}).text.strip('$')
        result['site'] = 'walmart'
        return result

