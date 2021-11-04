"""
Copyright (c) 2021 Anshul Patel
This code is licensed under MIT license (see LICENSE.MD for details)

@author: cheapBuy
"""

#Import libraries
from bs4 import BeautifulSoup
from threading import Thread
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from source.utils.url_shortener import shorten_url

#Set working directory path
import sys
sys.path.append('../')

class WebScrapper_Costco(Thread):
    """
    Main class used to scrape results from Costco
    
    ...

    Attributes
    ----------
    description : str
        description of the product
        
    Methods
    -------
    run:
        Threaded method to execute subclasses
    get_driver:
        Returns Chrome Driver
    get_url_costco:
        Returns costco URL
    scrap_costco:
        Returns Scraped result
    """
    
    def __init__(self,description):
        """
        Parameters
        ----------
        description : str
            description of the product
        """
        #Initialize class variables
        self.driver = self.get_driver()
        if len(description)<5:
            self.description = description
        else:
            self.description = ' '.join(description.split()[:5])
        self.result = {}
        super(WebScrapper_Costco,self).__init__()
        
    def run(self):
        """ 
        Returns final result
        """
        self.result={}
        try:
            #Get results from scrapping function
            results = self.scrap_costco()
            #Condition to check whether results are avialable or not
            if len(results) == 0:
                print('Costco_results empty')
                self.result={}
            else:                
                item=results[0]
                #Find teh atag containing our required item
                atag = item.find("span",{"class":"description"}).find('a')
                #Extract description from the atag
                self.result['description'] = atag.text
                #Get the URL for the page and shorten item
                self.result['url'] = atag.get('href')
                self.result['url'] = shorten_url(self.result['url'])
                #Find the price of the item
                self.result['price'] = item.find("div",{"class":"price"}).text.strip()
                #Assign the site as costco to result
                self.result['site'] = 'costco'
        except:
            print('Costco_results exception')
            self.result={}
            
    def get_driver(self):
        """ 
        Returns Chrome Driver
        """
        #Prepare driver for scrapping
        options = webdriver.ChromeOptions()
        options.headless = True
        driver = webdriver.Chrome(options=options, executable_path=ChromeDriverManager().install())
        return driver
    
    def get_url_costco(self):
        """ 
        Returns costco URL
        """
        #Prepare URL for given description
        template = "https://www.costco.com"+"/CatalogSearch?dept=All&keyword={}"
        search_term = self.description.replace(' ','+')
        return template.format(search_term)

    def scrap_costco(self):
        """ 
        Returns Scraped result
        """
        try:
            #Call the function to get URL
            url = self.get_url_costco()
            self.driver.get(url)
            #Use BeautifulSoup to scrap the webpage
            soup = BeautifulSoup(self.driver.page_source,"html.parser")
            results = soup.find_all('div',{'class': 'product-list grid'})
        except:
            results = []
        return results
        

