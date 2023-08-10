from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import urllib.request

import pandas as pd


chrome_options = Options()

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window() 

driver.get('https://www.daraz.com.bd/products/-i277201716-s1257142772.html')

scroll_height = driver.execute_script("return document.body.scrollHeight")

for i in range(0,scroll_height+1000,10):
    driver.execute_script(f'window.scrollTo(0, {i});')
    time.sleep(0.1)


elems = driver.find_elements(By.CLASS_NAME,value='content')
comments = []
for elem in elems:
    comments.append(elem.text)

print(comments)
time.sleep(30)

