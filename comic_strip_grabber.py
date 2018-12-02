# -*- coding: utf-8 -*-
"""
Garfield Spanish comic strip grabber
@author: Xarly

Format of the website: http://www.gocomics.com/garfieldespanol%20/2007/06/01
Image real link example: http://assets.amuniversal.com/39ae74c001cf01358d0a005056a9545d

Logs fields to the csv file
fields=['55/55/1999','http...','url img direction','captured','broken']
"""

import csv
import urllib.request
from sys import argv
from os import sep
from datetime import date, timedelta, datetime
from time import sleep
from requests import get as get_request
from bs4 import BeautifulSoup

print("Starting process")
check = True
capt = True

if len(argv) == 1:

    # Creation of the dates of the comics strips. Select the dates (short periods only pls, be nice to the web)
    year = 2017  # year of the desired comic strip
    d1 = date(year, 1, 1)  # start date %Y %m %d
    d2 = date(year, 1, 2)  # end date

else:
    d1 = datetime.strptime(argv[1], '%Y/%m/%d')
    d2 = datetime.strptime(argv[2], '%Y/%m/%d')

print("Parameters read: Start date {}, finish date {}".format(d1, d2))
delta = d2 - d1         # timedelta interval for the gathering


# Creation of the list with the links to get the comic strip
links_list = ["http://www.gocomics.com/garfieldespanol /" + (d1 + timedelta(days=i)).strftime("%Y/%m/%d")
              for i in range(delta.days + 1)]
    
# Loop to extract the pictures
for i in range(len(links_list)):
    sleep(0.2)
    page_request = get_request(links_list[i])
    soup = BeautifulSoup(page_request.content, 'html.parser')
    one = soup.findAll("picture")

    loop_img = str(one[1]).split(" ")[-3][5:-1]

    # Here we get the picture to the folder of the .py file
    try:
        if page_request.url != "http://www.gocomics.com/garfieldespanol /":
            output = "garf_" + links_list[i][-10:].replace("/", "_") + '.png'
            urllib.request.urlretrieve(loop_img, "extracted_images" + sep + output)
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
    if page_request.status_code != 200:
        link = "error web page"
    fields = [links_list[i][-10:], links_list[i], loop_img, str(capt), link]
    print(fields)

    with open("list_comics.csv", 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(fields)
