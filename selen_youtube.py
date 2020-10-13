from selenium import webdriver
from pathlib import Path
import re
import time
import youtube

DIR = Path(__file__).resolve().parent
URL_LIST_YOUTUBE = "https://www.youtube.com/watch?v=h8gE1WF7mBE&list=PL4C2OaC1jQqR3ICDBf4j1dH1Fk4uIo-Lx&index=101"


def start_chrome(url_youtube):
    global driver
    driver = webdriver.Chrome(DIR.joinpath('chromedriver'))
    driver.get(url_youtube)
    time.sleep(5)


def find_elements():
    """
        get all url on youtube video
    :return: array of strings
    """
    elements = driver.find_elements_by_xpath(
        "//a[@class='yt-simple-endpoint style-scope ytd-playlist-panel-video-renderer']")
    urls_youtube = []
    re_compile = re.compile(r'(.*)&list')
    for key in range(len(elements)):
        element = re_compile.findall(elements[key].get_attribute('href'))[0]
        urls_youtube.append(element)
    return urls_youtube


def pars_youtube(url):
    """
        parser youtube
    :param str url:
    :return: list urls from youtube
    """
    start_chrome(url)
    all_url = find_elements()
    driver.close()
    return all_url


youtube_url = pars_youtube(URL_LIST_YOUTUBE)
bad_url = []
for url in youtube_url:
    try:
        youtube.make_mp3_file(url)
    except:
        bad_url.append(url)
print(bad_url)
