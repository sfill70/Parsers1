import time
from time import sleep
import random
from Parser_organizations.get_driver import GetDriver




class ReceivingDataNalog:
    def __init__(self, inn_ogrn):
        self.data = inn_ogrn

    # Хорошо работает сохраняет в папку Загрузки ОС по умолчанию
    # def get_driver(self):
    #     driver = webdriver.Chrome()
    #     driver.wait = WebDriverWait(driver, sleep(random.uniform(3, 6)))
    #     driver.get("https://egrul.nalog.ru/index.html")
    #     return driver



    def receiving_data(self):
        # driver = self.get_driver()
        driver = GetDriver("https://egrul.nalog.ru/index.html").get_driver()
        list_organization = []
        id = self.data
        sleep(random.uniform(3, 6))
        # Ставим галочку точное повторение
        check_element = driver.find_element_by_id("unichk_0")
        check_element.click()
        sleep(random.uniform(3, 6))
        # Вводим название предприятия / инн /огрн
        input_element = driver.find_element_by_id("query")
        input_element.send_keys(id)
        sleep(random.uniform(3, 6))
        # Нажимаем поиск
        button_element = driver.find_element_by_id("btnSearch")
        button_element.click()
        sleep(random.uniform(3, 6))
        # получаем список кнопок "С загаловков организации" - кнопки дублируются element[0] = element[1] и т.д
        element1 = driver.find_elements_by_class_name("op-excerpt")
        # print(element1)
        # print(len(element1))
        # Клик по "Получение выписки" не всегда срабатывает по кнопке (элемент1[1]) тогда по названию
        isExcept = True
        try:
            element1[1].click()
            sleep(random.uniform(3, 6))
            isExcept = False
        except Exception as e:
            print(e)

        if isExcept:
            try:
                time.sleep(2)
                element1[0].click()
            except Exception as e:
                print(e)

        try:
            id = element1[0].text
        except Exception as e:
            print("0 " + str(e))


        brief_info_element = driver.find_elements_by_class_name("res-text")
        print(len(brief_info_element))
        with open('res.txt', 'w', encoding = 'utf-8') as ouf:
            ouf.write(str(id) + "!Имя! ")
            for inf in brief_info_element:
                list_organization.append(inf.text)
                ouf.write(str(inf.text) + '\n')


        driver.close()


# def main():
#     a = ReceivingDataNalog('5501160766')
#     a.receiving_data()
#
#
#
# if __name__ == '__main__':
#     main()
