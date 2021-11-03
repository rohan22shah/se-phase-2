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
from link_button import link_button


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
            price.append(float(result['price'].strip('$').rstrip('0')))
            site.append(result['site'])
        
    if len(price):
        
        def highlight_row(dataframe):
            #copy df to new - original data are not changed
            df = dataframe.copy()
            minimumPrice = df['Price'].min()
            #set by condition
            mask = df['Price'] == minimumPrice
            df.loc[mask, :] = 'background-color: green'
            df.loc[~mask,:] = 'background-color: ""'
            return df
        
        dataframe = pd.DataFrame({'Description': description, 'Price':price, 'Link':url}, index = site)
        st.balloons()
        st.subheader('RESULT')
        st.dataframe(dataframe.style.apply(highlight_row, axis=None))
        
        min_value = min(price)
        min_idx = [i for i, x in enumerate(price) if x == min_value]
        for minimum_i in min_idx:
            link_button(site[minimum_i], url[minimum_i])
        
    else:
        st.error('Sorry!, there is no other website with same product')
        