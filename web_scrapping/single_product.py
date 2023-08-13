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

driver.get('https://www.daraz.com.bd/smartphones/xiaomi-brand/')

# driver.get('file://F:/eshikhon_ml/web_scrapping/practice.html')

driver.maximize_window()

# title = driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div/div/div[1]/div[2]/div[1]/div/div/div[2]/div[2]/a').text

# tit = driver.find_element(By.TAG_NAME,'title').get_attribute('textContent')
# heading = driver.find_element(By.ID,'head').text
# paragraph = driver.find_element(By.TAG_NAME,'p').text
# link = driver.find_element(By.XPATH,'/html/body/a').get_attribute('href')
# image = driver.find_element(By.XPATH,'/html/body/img').get_attribute('src')

title = driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[3]/div[1]/div/div/div[2]/div[2]/a').text
link = driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[3]/div[1]/div/div/div[2]/div[2]/a').get_attribute('href')

img = driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[3]/div[1]/div/div/div[1]/div/a/img').get_attribute('src')

urllib.request.urlretrieve(img, "demo1.png")

driver.get(img)

print(title)
print(link)
print(img)

time.sleep(20)

