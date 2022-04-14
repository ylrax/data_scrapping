# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 20:42:14 2017

@author: Xarly

Generic quick test to check if the code and links extraction works properly
"""

import requests
from bs4 import BeautifulSoup

print("Reading example web...")
page_request = requests.get("http://www.gocomics.com/garfieldespanol /2000/1/1")
soup = BeautifulSoup(page_request.content, 'html.parser')
one = soup.findAll("picture")
if page_request.status_code == 200:
    print("Seems to work!! \n")
else:
    print("error code {}".format(page_request.status_code))

# Final check
print("extracted link: ", str(one[1]).split(" ")[-3][5:-1])
assert(str(one[1]).split(" ")[-3][5:-1] == "https://assets.amuniversal.com/457912605d20012ee3bd00163e41dd5b")
