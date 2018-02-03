# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 20:42:14 2017

@author: Xarly

generate dates since the beginning dec 1999
"""

import requests
from bs4 import BeautifulSoup


# Check with today comic to avoid invalid links to be resend (inexistent links goes to today's link)
page = requests.get("http://www.gocomics.com/garfieldespanol /2000/1/1")
soup = BeautifulSoup(page.content, 'html.parser')
one = soup.findAll("picture")

# old version:

B = []

for x in one:
    B.append(str(x))

p = B[1].split(" ")[4]
# contains the img link
print(p[13:])
print(p[13:] == "http://assets.amuniversal.com/457912605d20012ee3bd00163e41dd5b")

# or

print(str(one[1]).split(" ")[105][5:-1])
print(str(one[1]).split(" ")[105][5:-1] == "http://assets.amuniversal.com/457912605d20012ee3bd00163e41dd5b")
