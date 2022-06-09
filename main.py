from pytube import YouTube, Stream
import sys
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

channel = input("Enter youtube channel link: ")
path = input("Enter download path: ")
ask = input("Would you like audio only? (y or n): ")

downloadList = []

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--no-proxy-server')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("--mute-audio")
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument("--proxy-server='direct://'")
chrome_options.add_argument("--proxy-bypass-list=*")
chrome_options.add_argument("--proxy-bypass-list=*")
chrome_options.add_argument("test-type")
chrome_options.add_argument("--js-flags=--expose-gc")
chrome_options.add_argument("--enable-precise-memory-info")
chrome_options.add_argument("--disable-default-apps")
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
driver.get(channel)
time.sleep(4)
for WebElement in driver.find_elements(by=By.ID, value="""video-title"""):
    href = WebElement.get_attribute("href")
    downloadList.append(href)
yt = YouTube(downloadList[0])
path = os.path.join(path, yt.author)
os.mkdir(path)
if ask == "y":
    for link in downloadList:
        yt = YouTube(link)
        print(f"Currently Downloading: {yt.title}")
        a = yt.streams.get_audio_only()
        a.download(output_path=path)
else:
    for link in downloadList:
        yt = YouTube(link)
        print(f"Currently Downloading: {yt.title}")
        a = yt.streams.get_lowest_resolution()
        a.download(output_path=path)
sys.exit(0)
