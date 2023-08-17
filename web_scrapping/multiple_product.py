from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib.request
#from webdriver_manager.chrome import ChromeDriverManager
import time

from selenium.webdriver.chrome.service import Service

service = Service(executable_path='F:/eshikhon_ml/web_scrapping/chromedriver-win64/chromedriver.exe')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

# driver = webdriver.Chrome(executable_path='F:/eshikhon_ml/web_scrapping/chromedriver-win64/chromedriver.exe')



# driver.get('file://F:/eshikhon_ml/web_scrapping/practice.html')

driver.maximize_window()

title_list = []

link_list = []

price_list = []

for page in range(1,5):
    driver.get('https://www.daraz.com.bd/bags-luggage-luggage-sets/?page='+str(page))
    for i in range(1,41):
    #i should be type cast
        j=str(i)
        title = driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div/div/div[1]/div[2]/div['+j+']/div/div/div[2]/div[2]/a')
        title_list.append(title.text)

        # link = driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[3]/div['+j+']/div/div/div[2]/div[2]/a').get_attribute('href')

        link_list.append(title.get_attribute('href'))

        price = driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div/div/div[1]/div[2]/div['+j+']/div/div/div[2]/div[3]/span')

        price_list.append(price.text)

print(title_list)
print(len(title_list))


import pandas as pd

title_dict = {"title": title_list,'link':link_list,'price':price_list}

df = pd.DataFrame(title_dict)

df.to_csv('output.csv',index=False)

time.sleep(20)