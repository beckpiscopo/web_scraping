from bs4 import BeautifulSoup
from selenium import webdriver

import time

driver = webdriver.Chrome()

driver.get('https://treehouse-projects.github.io/horse-land/index.html')

# Use sleep() to give page time to load
time.sleep(5)

# Get the source of the page at the time it was read
page_html = driver.page_source

soup = BeautifulSoup(page_html, 'html_parser')

print(soup.prettify())

driver.close()