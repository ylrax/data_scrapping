# -*- coding: utf-8 -*-
"""
Garfield English old comic strip grabber
@author: Xarly

Format of the website: https://www.gocomics.com/garfield-classics/2018/11/26
Image real link image example: http://assets.amuniversal.com/39ae74c001cf01358d0a005056a9545d

Logs rows fields into the csv file
fields=['05/05/1979','http...','url img direction','captured','broken']

This section has the problem the the web publish the strips delayed. The date start is 20/06/2016 but it
is the 19/06/1978 comic strip (38 years and one day less).
From 01/01/2018 in advance there is only 38 years of delay
"""

import csv
import urllib.request
from sys import argv
from os import sep
from datetime import date, timedelta, datetime
from dateutil.relativedelta import relativedelta
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
delta = d2 - d1  # timedelta interval

# Creation of the list with the links to get the comic strip
links_list = ["http://www.gocomics.com/garfield-classics/" + (d1 + timedelta(days=i)).strftime("%Y/%m/%d")
              for i in range(delta.days + 1)]

# Loop to extract the pictures
for i in range(len(links_list)):
    sleep(0.2)
    page_request = get_request(links_list[i])
    soup = BeautifulSoup(page_request.content, 'html.parser')
    one = soup.findAll("picture")

    loop_img = str(one[1]).split(" ")[-3][5:-1]

    # Save the picture to the folder extracted_images from the home project folder
    try:
        if page_request.url != "https://www.gocomics.com/garfield-classics":
            if d1.year > 2017:
                output = "garf_" + (datetime.strptime(links_list[i][-10:], '%Y/%m/%d') +
                                    relativedelta(years=-38)).strftime("%Y_%m_%d") + '.png'
            else:
                output = "garf_" + (datetime.strptime(links_list[i][-10:], '%Y/%m/%d') +
                                    relativedelta(years=-38, days=-1)).strftime("%Y_%m_%d") + '.png'

            urllib.request.urlretrieve(loop_img, "extracted_images" + sep + output)
            capt = True
            link = "got it"
        else:
            capt = False
            link = "not in website"
            print(link)
            output = "     None"
    except:
        link = "fail"
        capt = False
        loop_img = ""
        output = "     None"

    # Now paste information in a csv as log file list_comics.csv (optional)
    if page_request.status_code != 200:
        link = "error web page"
    fields = [output[5:], links_list[i], loop_img, str(capt), link]
    print(fields)

    with open("list_first_comics.csv", 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(fields)
