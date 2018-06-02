#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 19:12:48 2018

@author: xingyichong
"""
from bs4 import BeautifulSoup as BS
import requests

EXCHANGE_URL = 'https://www.world-exchanges.org/home/index.php/members/wfe-members'

response = requests.get(EXCHANGE_URL)
soup = BS(response.content, 'html.parser')
raw = soup.find_all('li',{'data-lists-item':""})

def nameps(itersoup):  # generator for name
    for tag in raw:
        name = tag.find_all('span',{'style':'color:#0066a2'})
        if name:
            yield name[0].text.strip()
                   
def webps(itersoup):   # generator for website
    for tag in raw:
        web = tag.find_all('a')    
        if web:
            webn = web[0].text.strip()    
            if webn[0] == 'w' or webn[:3] == 'htt':
                yield webn
            

for i, (name, web) in enumerate(zip(nameps(raw), webps(raw))):
    print('[{0}] {1}  {2}'.format(i+1, name, web))
    
