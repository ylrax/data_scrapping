# Data_scrapping
Projects of data web scrapping
***

## Garfield comic strip scrapper


This python 3 script gets comic strips from 
a web and saves them into the computer as images.

There are no economical intentions on this project, 
all rights reserved to the owners of the content.


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

- Tests

To verify the correct performance of the code, there is 
a small test to be checked. Sometimes the web updates
the layout and the code stop working.

To launch the test:

```
python test/functionality_check.py
```

If no error are triggered, the the complete code 
should work, as now is explained.

- Functionality:

There are two versions of the code:

1. New daily comic strip grabber:

With the file *comic_strip_grabber.py* daily Spanish
comics strips are gathered.

Usage:

Configure the date parameters inside the file
 and execute it
```
python comic_strip_grabber.py
```
or give it parameters (start dates and end date) 
on the call with format *'%Y/%m/%d'*:
```
python comic_strip_grabber.py "2017/01/01" "2017/01/02"
```

2. First old english comic strips

With the file *classic_emg_first_strips.py* older 
English comics strips are gathered. 
The launch is the same as the previous one:

Configure the date parameters inside the file
 and execute it
```
python classic_emg_first_strips.py
```
or give it parameters (start dates and end date) 
on the call with format *'%Y/%m/%d'*:
```
python classic_emg_first_strips.py "2017/01/01" "2017/01/02"
```

## Output

Comic strips are stored inside the folder 
*extracted_images* as PNG images and format: 
"garf_date.png"

Also all logs and information are stored into a scv file.
