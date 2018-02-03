# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 20:42:14 2017

@author: Xarly

generate dates since the beginning dec 1999
"""

# format: http://www.gocomics.com/garfieldespanol%20/2007/06/01
from datetime import date, timedelta
import csv

d1 = date(2008, 8, 17)  # start date
d2 = date(2008, 8, 20)  # end date

delta = d2 - d1  # timedelta
li = ["http://www.gocomics.com/garfieldespanol /" + (d1 + timedelta(days=i)).strftime("%Y/%m/%d")
      for i in range(delta.days + 1)]

# dat=li[4][-10:]
print(li)

fields = ['55/55/1999', 'http...', 'captured', 'broken']

with open("list_comics_test.csv", 'a', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(fields)

with open('list_comics_test.csv') as f:
    print(f.read())
