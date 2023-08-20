from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib.request
#from webdriver_manager.chrome import ChromeDriverManager
import time

from selenium.webdriver.chrome.service import Service

service = Service(executable_path='F:/eshikhon_ml/web_scrapping/chromedriver-win64/chromedriver.exe')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.get('https://climate.weather.gc.ca/historical_data/search_historic_data_stations_e.html?searchType=stnProv&timeframe=1&lstProvince=ON&optLimit=yearRange&StartYear=2019&EndYear=2023&Year=2023&Month=8&Day=19&selRowPerPage=25')


driver.maximize_window()
title_list = []
for i in range(2,28):
    formatted_string = f'"stnRequest{i}"'
    # print(formatted_string)
    # concat = '"stnRequest"'  str(i)
    value = '//*[@id='+formatted_string+']/div[1]'
    # result = f'"{value}"'
    # # formatted_string = value.replace(concat, '"stnRequest1"')
    # print(value)
    # print(formatted_string)
    # print(result)
    try:
        title = driver.find_element(By.XPATH,'/html/body/main/div[1]/div['+str(i)+']/form/div[1]')
        title_list.append(title.text)
    except:
        print("Something else went wrong")


import pandas as pd

title_dict = {"title": title_list}

df = pd.DataFrame(title_dict)

df.to_csv('station.csv',index=False)

time.sleep(20)

# print(title.text)