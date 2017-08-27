# -*- coding: utf-8 -*-
"""
Garfield spanish comic strip capturer
@author: Xarly

Format of the website: http://www.gocomics.com/garfieldespanol%20/2007/06/01
#image link example: http://assets.amuniversal.com/39ae74c001cf01358d0a005056a9545d
fields=['55/55/1999','http...','url img direction','captured','broken']
"""

from datetime import date, timedelta
import time
import requests
from bs4 import BeautifulSoup
import csv   
import urllib.request

#creation of the dates of the comics strips. Select the dates (short periods only pls)
check=True
capt=True
year=2016

d1 = date(year, 1, 1)  # start date %y %m %d
d2 = date(year, 2, 28)  # end date

#master online
#branch 1

delta = d2 - d1         # timedelta
li=[]

#for i in tqdm.tqdm(range(delta.days + 1)):
for i in range(delta.days + 1):    
    temp=d1 + timedelta(days=i)
    li.append("http://www.gocomics.com/garfieldespanol /"+temp.strftime("%Y/%m/%d"))
    
    
#check with today comic to avoid invalid links to be resend
pag = requests.get("http://www.gocomics.com/garfieldespanol")   
soup = BeautifulSoup(pag.content, 'html.parser')
one=soup.findAll("picture")
B=[]

for x in one:
    B.append(str(x))

p=B[1].split(" ")[4]
#p[5:-1] contains the today's img link
    
    
for i in range(len(li)):
    time.sleep(0.2)
    pag = requests.get(li[i])   
    soup = BeautifulSoup(pag.content, 'html.parser')

    one=soup.findAll("picture")
    A=[]

    for x in one:
        A.append(str(x))

    t=A[1].split(" ")[4]
    #t[5:-1] contain the img link
    
    
    #here we get the picture to the folder of the .py file
    try:
        if t[5:-1]!=p[5:-1]:
            output="garf_"+li[i][-10:].replace("/", "_")+'.png'
            urllib.request.urlretrieve(t[5:-1],output)
            capt=True
            link="got it"
        else:
            capt=False
            link="not in website"
            print(link)
            t=""
    except:
        link="fail"
        capt=False
        t=""
    
     # now paste information in a csv (optional)
    if pag.status_code!=200:
        link="error webpage"
    fields=[li[i][-10:],li[i],t[5:-1],str(capt),link]

    with open("list_comics.csv", 'a',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(fields)
