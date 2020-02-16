from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Firefox()
driver.get('https://www.livejournal.com/rsearch?q=%D0%B3%D0%B0%D0%B7%D0%BF%D1%80%D0%BE%D0%BC%D0%BD%D0%B5%D1%84%D1%82%D1%8C&searchArea=post')
time.sleep(10)
data=driver.find_element_by_xpath('//*[@id="js"]/body/div[2]/div[5]/div[1]/div/section/div/div[2]/ul/li[3]/div/p/span').text
driver.get('https://www.reverso.net/text_translation.aspx?lang=RU')
data1=driver.find_element_by_class_name('ru').get_attribute('href')
print(data, data1)
