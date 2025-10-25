import sys
from os import environ, listdir, path
from time import sleep

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

if len(sys.argv) == 1:
    print("No default argument passed!!")
    print("Using the environment variables")
    FOLDER_PATH = environ.get("FOLDER_PATH", '/tmp')
    URL = environ.get("URL", 'https://www.natomanga.com/manga/black-fox-sword-master-of-mount-kunlun')
    CHAPTERS_LIMIT = environ.get("URL", 5)

else:
    FOLDER_PATH = sys.argv[1]
    URL = sys.argv[2]
    try:
        CHAPTERS_LIMIT = int(sys.argv[3])
    except IndexError:
        print("Default limit 5")
        CHAPTERS_LIMIT = 5

# cd C:\Users\Xarly\Documents\repos\data_scrapping\online_manga\
# python -m selenium_test.py "Z:\JD\Star embracing Swordmaster" "https://www.natomanga.com/manga/star-embracing-swordmaster" 5

print("    Arguments:")
print(FOLDER_PATH)
print(URL)
print(CHAPTERS_LIMIT)

def get_max_saved_chapter(target_path):
    """Extracts the maximun chapter available on
    a path"""

    try:
        files_in_path = listdir(target_path)

        if "-Page_" in files_in_path[0]:
            print("Page files format")
            return max([float(files_chapter.split("-Page_")[0].split(" ")[-1]) if ";" not in files_chapter else float(files_chapter.split(";")[0].split(" ")[-1]) for files_chapter in files_in_path])

        return float(max([files_chapter.split("_")[1] for files_chapter in files_in_path]))
    except IndexError:
        return 0.0


MAX_SAVED_CHAPTER = get_max_saved_chapter(FOLDER_PATH)
print(MAX_SAVED_CHAPTER)


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--window-size=1920,1080')
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument("--log-level=2") # supress extra warnings
#chrome_options.add_argument('--headless')
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument('--profile-directory=Default')
chrome_options.add_argument("--incognito")
chrome_options.add_argument('--disable-dev-shm-usage')


driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)
sleep(59)


chapters = driver.find_element(by=By.CLASS_NAME, value="chapter-list")
elements = chapters.find_elements(By.CLASS_NAME, 'row')

chapters_list = [URL + "/" + e.find_elements(by=By.TAG_NAME, value="span")[0].text.lower().replace(" ", "-").replace(".", "-") for e in elements]


chapters_list_filtered = [l for l in reversed(chapters_list) if float(l.split("-")[-1]) > MAX_SAVED_CHAPTER]

print("Total chapters found: ", len(chapters_list),
       "Max chapter in web: ",max([ float(l.split("-")[-1]) for l in reversed(chapters_list)]),
       "chapters filtered: ",  len(chapters_list_filtered))


if len(chapters_list_filtered)>CHAPTERS_LIMIT:
    extractable_chapters_list_filtered = chapters_list_filtered[0:CHAPTERS_LIMIT]
else:
    print("Less chapters available than chapter max limits")
    if max([ float(l.split("-")[-1]) for l in reversed(chapters_list)]) == MAX_SAVED_CHAPTER:
        print("NO more chapters available!!!!")
        driver.quit()
        sys.exit(0)
    extractable_chapters_list_filtered = chapters_list_filtered


driver.get(extractable_chapters_list_filtered[0])
print("Opening for cookie: ", extractable_chapters_list_filtered[0])
sleep(9)
try:
    COOKIE = driver.get_cookie("__cflb")["value"]
except TypeError:
    print("Error in cookie, retry...")
    driver.get_cookies()
    sleep(9)
    COOKIE = driver.get_cookie("__cflb")["value"]

driver.quit()

print("Exit explorer")

def extract_images_path_option(url):
    """Return the list of images on a comic URL"""

    request = requests.get(url)
    if request.status_code!=200:
        print("Error")

    soup = BeautifulSoup(request.content, 'html.parser')

    image_urls_list = []
    for image in soup.find_all("div", {"class": "container-chapter-reader"})[0].find_all("img"):
        image_urls_list.append(image["src"])

    return image_urls_list

BASE_URL = "https://www.natomanga.com/"
cookies = {
    "__cflb": COOKIE,
}


files = listdir(FOLDER_PATH)

# fix it
if len(files)!=0:
    if "-Page_" in files[0]:
        root_name = files[0].split("_Chapter")[0] + "_Chapter "
        img_path_zero_fill = "-Page_"
    else:
        root_name = "chapter_"
        img_path_zero_fill = "_"
else:
    root_name = "chapter_"
    img_path_zero_fill = "_"

print("    START THE LOOP")

for n_chap, chap in enumerate(extractable_chapters_list_filtered):
    print(chap)
    image_urls = extract_images_path_option(chap)
    print("For", len(image_urls), "images.", " Step ", n_chap, "/", len(extractable_chapters_list_filtered))

    chapter = chap.split("-")[-1]

    with requests.Session() as session:
        for n, p in enumerate(image_urls):
            print(n, p, chapter)
            file_extension = path.splitext(p)[1]
            resp_2 = session.get(p,
                        headers={"referer": BASE_URL,
                        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
                        'Accept-Language': 'en-US,en;q=0.5',
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8'},
                        cookies=cookies)
            if resp_2.status_code!=200:
                print("Retry error", resp_2.status_code)
                sleep(2)
                resp_2 = session.get(p,
                                headers={"referer": BASE_URL,
                                'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
                                'Accept-Language': 'en-US,en;q=0.5',
                                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8'},
                                cookies=cookies)
                if resp_2.status_code!=200:
                    print("Again error", resp_2.status_code)

            with open(r"{}\{}{:0>4}{}{:0>3}{}".format(FOLDER_PATH, root_name, chapter, img_path_zero_fill, n, file_extension), 'wb') as outfile:
                outfile.write(resp_2.content)

            sleep(1)
    print("chapter {} finished".format(chapter))
    sleep(5)


print("THE END!!!")
