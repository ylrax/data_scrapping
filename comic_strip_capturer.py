# -*- coding: utf-8 -*-
"""
Garfield spanish comic strip capturer
@author: Xarly

Format of the website: http://www.gocomics.com/garfieldespanol%20/2007/06/01
Image real link example: http://assets.amuniversal.com/39ae74c001cf01358d0a005056a9545d

Logs fields to the csv file
fields=['55/55/1999','http...','url img direction','captured','broken']
"""

from datetime import date, timedelta
import time
import requests
from bs4 import BeautifulSoup
import csv   
import urllib.request

print("Starting process")
# Creation of the dates of the comics strips. Select the dates (short periods only pls, be nice)
check = True
capt = True
year = 2016  # year of the desired comic strip

d1 = date(year, 1, 1)  # start date %y %m %d
d2 = date(year, 1, 1)  # end date

delta = d2 - d1         # timedelta interval for the gathering


# Creation of the list with the links to get the comic strip
li = ["http://www.gocomics.com/garfieldespanol /" + (d1 + timedelta(days=i)).strftime("%Y/%m/%d")
      for i in range(delta.days + 1)]
    
    
# Check with today comic to avoid invalid links to be resend (inexistent links goes to today's link)
pag = requests.get("http://www.gocomics.com/garfieldespanol")
soup = BeautifulSoup(pag.content, 'html.parser')
one = soup.findAll("picture")

# contains the today's img link
today_img = str(one[1]).split(" ")[105][5:-1]
    
# Loop to extract the pictures
for i in range(len(li)):
    time.sleep(0.2)
    pag = requests.get(li[i])   
    soup = BeautifulSoup(pag.content, 'html.parser')
    one = soup.findAll("picture")

    loop_img = str(one[1]).split(" ")[105][5:-1]

    # Here we get the picture to the folder of the .py file
    try:
        if today_img != loop_img:
            output = "garf_" + li[i][-10:].replace("/", "_") + '.png'
            urllib.request.urlretrieve(loop_img, output)
            capt = True
            link = "got it"
        else:
            capt = False
            link = "not in website"
            print(link)
            t = ""
    except:
        link = "fail"
        capt = False
        loop_img = ""
    
    # Now paste information in a csv as log file list_comics.csv (optional)
    if pag.status_code != 200:
        link = "error web page"
    fields = [li[i][-10:], li[i], loop_img, str(capt), link]
    print(fields)

    with open("list_comics.csv", 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(fields)
