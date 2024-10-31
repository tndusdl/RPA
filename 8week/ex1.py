from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

url = 'https://www.google.co.kr/'
driver = webdriver.Chrome()
driver.get(url)
time.sleep(3)

search_box = driver.find_element(By.CSS_SELECTOR, '#APjFqb')
search_box.send_keys("KBO 한국시리즈")
search_box.send_keys(Keys.RETURN)
time.sleep(20)