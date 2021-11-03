    # -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 14:34:03 2021

@author: patel
"""


# Import Libraries
import streamlit as st
import os
from web_scrappers.WebScrapper import WebScrapper
import pandas as pd

# Hide Footer in Streamlit
hide_menu_style = """
        <style>
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

# Add footer to UI
footer="""<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: black;
color: white;
text-align: center;
}
</style>
<div class="footer">
<p>Developed with ❤ by <a style='display: block; text-align: center;' href="https://github.com/anshulp2912/scrivener" target="_blank">Scrivener</a></p>
<p><a style='display: block; text-align: center;' href="https://github.com/anshulp2912/scrivener/blob/main/LICENSE" target="_blank">MIT License Copyright (c) 2021 Anshul Patel</a></p>
<p>Contributors: Anshul, Bhavya, Darshan, Pragna, Rohan</p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)

url = st.text_input('Enter the product website link')

# Pass url to method
if url:
    webScrapper = WebScrapper(url)
    results = webScrapper.call_scrapper()

    # Use st.columns based on return values
    description = []
    url = []
    price = []
    site = []
    
    for result in results:
        if result is not None:
            description.append(result['description'])
            url.append(result['url'])
            price.append(result['price'])
            site.append(result['site'])
        
    if len(price):
        dataframe = pd.DataFrame({'Site':site,  'Price':price, 'Link':url})
        st.table(dataframe)
    else:
        st.error('Sorry!, there is no other website with same product')
        