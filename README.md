# Data_scrapping
Projects of data web scrapping


![npm bundle size](https://img.shields.io/badge/python-3.9.0-success?logo=python)
***

## Garfield comic strip scrapper


This python script gets comic strips from a webpage and saves them into the computer as images.
There are no economical intentions on this project, all rights reserved to the owners of the content.


- Requisites:

Python 3 code tested with the libraries (it may work with other versions):
```
beautifulsoup4==4.6.3
requests==2.20.1
urllib3==1.24.1
```
Library installation process:
```
pip install beautifulsoup4==4.6.3 requests==2.20.1 urllib3==1.24.1
```

- Tests and checks

To verify the correct performance of the code, there is a small test to be checked. Sometimes the web updates the layout and the code stop working.

To launch the test:

```
python comic_strips/test/functionality_check.py
```

If no error are triggered, the the complete code should work, as now is explained.


### Execution:

There are two versions of the code:

1. New daily comic strip grabber:

With the file *comic_strip_grabber.py* daily Spanish comics strips are gathered.

Usage:

Configure the date parameters inside the file  and execute it
```
python comic_strips/comic_strip_grabber.py
```
or give it parameters (start dates and end date) on the call with format *'%Y/%m/%d'*:
```
python comic_strips/comic_strip_grabber.py "2017/01/01" "2017/01/02"
```

2. First old english comic strips

With the file *classic_emg_first_strips.py* older English comics strips are gathered. 
The launch is the same as the previous one:

Configure the date parameters inside the file and execute it
```
python comic_strips/classic_emg_first_strips.py
```
or give it parameters (start dates and end date) on the call with format *'%Y/%m/%d'*:
```
python comic_strips/classic_emg_first_strips.py "2017/01/01" "2017/01/02"
```

### Output

Comic strips are stored inside the folder *extracted_images* as PNG images and format: 
"garf_YYYY_MM_DD.png"

Also all logs and information are stored into a scv file.


***

## Manga chapter scrapper

(WIP) Currently there is a notebook under the folder online_manga that extracts full chapters from online viewers ands saves them as images locally.