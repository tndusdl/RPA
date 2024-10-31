from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

query = input('검색할 키워드를 입력하세요: ')

url ='https://www.naver.com/'
driver = webdriver.Chrome()
driver.get(url)
time.sleep(3)

search_box = driver.find_element(By.CSS_SELECTOR,'#query')
search_box.send_keys(query)
search_box.send_keys(Keys.RETURN)
time.sleep(2)

# 뉴스 탭 클릭
driver.find_element(By.CSS_SELECTOR,'#lnb > div.lnb_group > div > div.lnb_nav_area._nav_area_root > div > div.api_btn_page._nav_btn_root > div.btn_next._next > a > span > i').click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR,'#lnb > div.lnb_group > div > div.lnb_nav_area._nav_area_root > div > div.api_flicking_wrap._conveyer_root > div:nth-child(8) > a').click()
time.sleep(3)

# 텍스트와 링크 가져오기
news_title = driver.find_elements(By.CSS_SELECTOR,".news_tit")
print(news_title)

for i in news_title :
      title = i.text
      href = i.get_attribute('href')
      print(title , ":", href)