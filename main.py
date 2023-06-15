import random
import os
from bs4 import BeautifulSoup
import requests
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pyautogui

#selenium environment

chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--headless")


driver = webdriver.Chrome(chrome_options=chrome_options)




articles = []
if 'url.txt' not in os.listdir():
    url = 'https://en.wikipedia.org/wiki/Special:AllPages?from=&to=&namespace=0'
else:
    with open('url.txt', 'r') as url_text:
            url = url_text.read()
    url = url
prev_url = ''

#start
driver.get(url)
if 'wiki_articles.txt' not in os.listdir():
    next_page = driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[2]/a')
    next_page.click()
#start at current url
else:
    next_page = driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[2]/a[2]')
    next_page.click()

while url != prev_url:
    wiki = requests.get(url)
    soup = BeautifulSoup(wiki.text, 'html.parser')

    all_pages = BeautifulSoup(soup.find('ul', class_='mw-allpages-chunk').prettify(), 'html.parser')
    all_pages = all_pages.find_all('a')


    for page in all_pages:
        article = page.text.strip()
        if article not in articles:
            articles.append(article)
    next_page = driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[2]/a[2]')
    next_page.click()
    prev_url = url
    url = driver.current_url
    with open('url.txt', 'w') as saved_url:
            saved_url.write(str(url))
    print(len(articles))
    print(url)
    #get new url
    pyautogui.moveTo((random.randint(1,1000),random.randint(1,1000)))
    # Open the file in write mode
    if 'wiki_articles.txt' in os.listdir():
        existing_items = set()
        with open('wiki_articles.txt', "r") as existing_articles:
            for line in existing_articles:
                existing_items.add(line.strip())
        print('existing articles: ', len(existing_items))
        with open('wiki_articles.txt', 'a') as existing_articles:
            for item in articles:
                if item not in existing_items:
                    existing_articles.write(item + "\n")
                    existing_items.add(item)
    else:
        with open('wiki_articles.txt', 'a') as file:
            # Iterate over the list and write each element to a new line
            for item in articles:
                file.write(str(item) + '\n')
    driver.get(url)

