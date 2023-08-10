from selenium import webdriver
from selenium.webdriver.common.by import By
#from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(executable_path='F:/eshikhon_ml/web_scrapping/chromedriver-win64/chromedriver.exe')

driver.get('https://www.daraz.com.bd/men-muslimin-shirts/')

driver.maximize_window()

title = driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div/div/div[1]/div[2]/div[1]/div/div/div[2]/div[2]/a').text

print(title)

time.sleep(20)

