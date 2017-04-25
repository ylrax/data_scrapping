# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 20:42:14 2017

@author: Xarly

generate dates since the beggining dec 1999
"""

#format: http://www.gocomics.com/garfieldespanol%20/2007/06/01
from datetime import date, timedelta


d1 = date(2008, 8, 15)  # start date
d2 = date(2008, 8, 25)  # end date

delta = d2 - d1         # timedelta
li=[]

for i in range(delta.days + 1):
    temp=d1 + timedelta(days=i)
    li.append("http://www.gocomics.com/garfieldespanol /"+temp.strftime("%Y/%m/%d"))
li 
#dat=li[4][-10:]

import csv   
fields=['55/55/1999','http...','captured','broken']

with open("list_comics.csv", 'a',newline='') as f:
    writer = csv.writer(f)
    writer.writerow(fields)
    
with open('list_comics.csv') as f:
    print(f.read())