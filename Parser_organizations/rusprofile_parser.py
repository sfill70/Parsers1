
from time import sleep
import random


import os

from .get_driver import GetDriver


class RusprofilParser(object):
    def __init__(self, inn_ogrn, is_courts=True):
        self.data = inn_ogrn
        self.is_courts = is_courts



    def parsing(self):
        # driver = self.get_driver()
        driver = GetDriver("https://www.rusprofile.ru/").get_driver()
        dict_organization_reliability = dict()
        id = self.data
        sleep(random.uniform(3, 6))
        input_element = driver.find_element_by_class_name("index-search-input")
        input_element.send_keys(id)
        sleep(random.uniform(3, 6))
        button_element = driver.find_element_by_xpath("//*[@id='indexsearchform']/button")
        button_element.click()
        sleep(random.uniform(6, 8))
        driver.refresh()
        ur = driver.current_url
        print(ur)
        if not ("https://www.rusprofile.ru/id/" in str(ur)):
            print()
            check_element = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div[1]/label/span")
            check_element.click()
        sleep(random.uniform(4, 6))
        # Кнопки двигаются
        button_element_reliability = ''
        for n in range(1, 6):
            # button_element_reliability = driver.find_element_by_xpath(
            #     "/html/body/div[2]/div/div/div[1]/div[2]/nav/a[{}]".format(str(n)))
            # button_element_reliability = driver.find_element_by_xpath(
            #     "/html/body/div[2]/div/div/div[1]/div[2]/nav/a[%s]"%(str(n)))
            button_element_reliability = driver.find_element_by_xpath(
                "/html/body/div[2]/div/div/div[1]/div[2]/nav/a[" + str(n) + "]")
            if str(button_element_reliability.text).lower() == "надежность":
                break

        button_element_reliability.click()
        sleep(random.uniform(4, 6))

        name_organ = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div[1]/h1/a')
        print(name_organ.text)
        item_elemrnts = driver.find_elements_by_class_name("requisites-item__name")
        # print(len(item_elemrnts))
        for item in item_elemrnts:
            # print(item.text)
            ar_item = []
            try:
                ar_item = str(item.text).split('\n')
                dict_organization_reliability[ar_item[0]] = ar_item[1]
            except Exception as e:
                print(e, end=' - ')
                print(item)

        # print(dict_organization_reliability)
        sleep(random.uniform(1, 3))
        map_courts = dict()
        is_yes = False
        if self.is_courts:
            button_element_courts = ''
            for n in range(2, 7):
                button_element_courts = driver.find_element_by_xpath(
                    "/html/body/div[2]/div/div/div[1]/div[2]/nav/a[%s]/span" % (str(n)))
                # print(button_element_courts.text)
                sleep(random.uniform(1, 2))
                if str(button_element_courts.text).lower() == 'суды':
                    is_yes = True
                    break
            if is_yes:
                button_element_courts.click()
                sleep(random.uniform(6, 8))
                # url_courts = driver.current_url
                # print(url_courts)
                courts_element = driver.find_elements_by_class_name("company-item")
                try:
                    print(len(courts_element))
                except:
                    print()
                key = ""
                volume = ""
                for element in courts_element:
                    key_el = element.find_element_by_class_name("license-name")
                    try:
                        key = key_el.text
                    except Exception as e:
                        print(e)

                    volume_el = element.find_element_by_class_name("out-link")
                    try:
                        volume = volume_el.get_attribute("href")
                    except Exception as e:
                        print(e)
                    try:
                        map_courts['Дело № ' + str(key)] = str(volume)
                    except Exception as e:
                        print(e)
                    # print(map_courts)
            else:
                print("Судов не обнаружено")
                map_courts['Судов'] = 'Не обнаружено'
            dict_organization_reliability.update(map_courts)
        else:
            print("Суды не запрошены")
            map_courts['Суды'] = 'Не запрошены'

        driver.close()
        print(dict_organization_reliability)
        return dict_organization_reliability


def main():
    # inn = 1106014140
    # inn = 7710035963
    # inn = 5031115441
    # inn = 5053000797
    # inn = 5031115441
    inn = 1106014140
    # inn = 7722743350
    a = RusprofilParser(inn, True)
    dik = a.parsing()

    file_name = os.path.join(os.getcwd(), str(inn) + '_reliability' + '.txt')
    for key in dik:
        with open(file_name, 'a', encoding='utf-8') as ouf:
            ouf.write(key + " : " + dik[key] + '\n')


if __name__ == '__main__':
    main()
