#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 17:14:14 2018

@author: xingyichong
"""

from bs4 import BeautifulSoup as BS
import requests

#grab data from HTML file that was downloaded in local drive.
#soup = BeautifulSoup(open('/Users/xingyichong/downloads/WFE Members.html'))
#soup.prettify
url = 'https://www.world-exchanges.org/home/index.php/members/wfe-members'

response = requests.get(url)
soup = BS(response.content, 'html.parser')



# Final approach
Original_Search = soup.find_all('li',{'data-lists-item':""})

f1 = [x.find_all('span',{'style':'color:#0066a2'}) for x in Original_Search]   #f1 is for getting exchange name       
Ex_name = [x[0].text.strip() for x in f1 if x!=[]] # if the result is not blank, put into the name list
f2 = [x.find_all('a') for x in Original_Search]        # f2 is for getting website address
Ex_website = [x[0].text.strip() for x in f2 if x!=[]]  # if the result is not blank, put into the website list
Ex_website = [x for x in Ex_website if x[0]=='w' or x[0:3]=='htt']

# map into the dict
Ex_map = {}
try:
    len(Ex_website) == len(Ex_name)
    for i in range(0,len(Ex_website)-1):
        Ex_map[Ex_name[i]] = Ex_website[i]
except ValueError:
    print('The length of namelist and website cannot match!')

print(Ex_map)


'''
Below, the old approach 2, which is less clean.

split_list=[]
exchng_list={}
name_list=[]

for exn in mysc:
    split_list.append(exn.text)

xi = 0
for l in split_list:  
    xi += 1
    if '+' in l:
        break
    
          
for l in split_list[xi-1:]:        
    sp = l.split('+')
    if len(sp)<2:
        break
    exchng_list[sp[0][2:]] = sp[1][4:len(sp[1])-5]
    name_list.append(sp[0][2:])
   
    

print(name_list)
print('The running time is %.2f second.' % (time.time()-ST))

   
'''
'''
# Approach 1
Exchange_list=[]
for exname in soup.find_all('span',{'style':"color:#0066a2"}):
        Exchange_list.append(exname.text)

while Exchange_list.pop() != 'How We Use Cookies':
    Exchange_list.pop()
    
print(len(Exchange_list))
'''

'''
tried multiprocessing:
    
def add1(list1, list2):
    list1[list2[0][2:]] = list2[1][4:len(list2[1])-5]

    p1 = multiprocessing.Process(target = add1, args = (exchng_list, sp))
    p2 = multiprocessing.Process(target = name_list.append(sp[0][2:]))
    p1.start
    p2.start

'''
'''
this is the HTML sample from the target website:
    
    
<li data-lists-item="">

<h4 class="sprocket-lists-title padding" data-lists-toggler="">
<span style="color:#0066a2">Taiwan Futures Exchange</span> <span class="indicator"><span>+</span></span> </h4>

    
<div class="sprocket-lists-item" data-lists-content="">
<div class="sprocket-padding">
<img alt="" height="71" src="/home/2015/files/logo/TAIFEX%20Logo%20-03-2012.jpg" width="264"/><p><a href="http://www.taifex.com.tw" target="_blank">www.taifex.com.tw</a></p> </div>
</div>

</li>

'''
