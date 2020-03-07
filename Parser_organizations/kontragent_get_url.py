import random
from time import sleep
import os
from Parser_organizations.get_driver import GetDriver


class KontragentGetUrl(object):
    
    def __init__(self, inn_ogrn):
        self.inn_ogrn = str(inn_ogrn)

    
    def get_url(self):
        global button_element
        # driver = webdriver.Chrome()
        # driver.wait = WebDriverWait(driver, random.uniform(3, 6))
        # driver.get("https://kontragent.skrin.ru/dbsearch/dbsearchru/companies/")
        driver = GetDriver("https://kontragent.skrin.ru/dbsearch/dbsearchru/companies/").get_driver()
        input_element = driver.find_element_by_id("comp")
        input_element.send_keys(self.inn_ogrn)
        input_element1 = driver.find_element_by_class_name("btns")
        input_element1.click()
        sleep(random.uniform(3, 6))

        page_element1 = driver.find_elements_by_xpath("//a[@class='comp_title']")
        url = ""
        for el in page_element1:
            try:
                url = el.get_attribute('href')

            except:
                pass

        driver.close()
        print(url)
        return url







# def main():
#      url = KontragentGetUrl('7706043263').get_url()
#      print(url)
#
#
# if __name__ == '__main__':
#     main()
