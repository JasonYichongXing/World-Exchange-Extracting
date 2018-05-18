#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 17:14:14 2018

@author: xingyichong
"""

from bs4 import BeautifulSoup as BS
import requests
import pprint

EXCHANGE_URL = 'https://www.world-exchanges.org/home/index.php/members/wfe-members'

response = requests.get(EXCHANGE_URL)
soup = BS(response.content, 'html.parser')

Original_Search = soup.find_all('li',{'data-lists-item':""})

f1 = [x.find_all('span',{'style':'color:#0066a2'}) for x in Original_Search]   #f1 is for getting exchange name       
Ex_name = [x[0].text.strip() for x in f1 if x!=[]] 
f2 = [x.find_all('a') for x in Original_Search]        # f2 is for getting website address
Ex_website = [x[0].text.strip() for x in f2 if x!=[]]  
Ex_website = [x for x in Ex_website if x[0]=='w' or x[0:3]=='htt']

results = dict(zip(Ex_name,Ex_website))

pprint.pprint(results)
