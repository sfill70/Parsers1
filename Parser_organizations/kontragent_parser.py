import requests
from bs4 import BeautifulSoup
import os
import re
from time import sleep
import random
from Parser_organizations.kontragent_get_url import KontragentGetUrl

headers = {'accept': '*/*',
           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}


class KontragentParser(object):

    def __init__(self, inn):
        self.inn = inn
        self.url = KontragentGetUrl(inn).get_url()

    def parser(self):
        global soup
        url = self.url
        # url = "https://kontragent.skrin.ru/issuers/URAM"
        session = requests.Session()
        request = session.get(url, headers=headers)
        if request.status_code == 200:
            sleep(random.uniform(3, 6))
            print("ok")
            soup = BeautifulSoup(request.content, 'html.parser')

            clas_div = soup.find_all("div", attrs={'class': 'info_block'})

            map_fin = dict()

            def array_to_map(array, map):
                if len(array) > 1:
                    line = ""
                    for i in range(1, len(array)):
                        line = line + str(2018 + i - len(array) + 1) + " год " + re.sub('\\s+', ' ',
                                                                                        str(array[i]).strip()) + ", "

                    map[re.sub('\\s+', ' ', str(array[0]).strip())] = line[:-2]
                return map

            def map_fin_filling(tag_fin):
                array = []
                tag_tr = tag_fin.find_all("tr")
                for tr in tag_tr:
                    # print(tr)
                    td = tr.find_all("td")
                    for txt in td:
                        array.append(txt.text)
                    array_to_map(array, map_fin)
                    # print(array)
                    array = []

            map_akchioner = dict()

            def in_map_akchioner(td, map_akchioner):
                array_akchioner = []
                key = ""
                try:
                    tr = td.find("tr")
                    key = re.sub('\n\s+|\r\s+', '   ', str(tr.text).strip()).replace("  ", ",")
                    # print(key)
                except:
                    pass
                td = td.find("tbody")
                for tag in td:
                    try:
                        if not tag.is_empty_element:
                            at = re.sub(r'\n+', '\n ', str(tag.text).strip()).split('\n')
                            array_akchioner.append([re.sub('\\s+', ' ', i) for i in at[0:len(at) + 1] if
                                                    re.sub('\\s+', ' ', i) != ' ' and re.sub('\\s+', ' ', i) != ' - '])
                    except:
                        pass

                map_akchioner[key] = str(array_akchioner)[1:-1].replace('\'', '')
                # print(array_akchioner)
                return map_akchioner

            for tag in clas_div:
                if "финансовые показатели" in tag.text.lower():
                    tag_fin = tag
                    map_fin_filling(tag_fin)
                elif "учредителя или участника" in tag.text.strip().lower().replace("  ", " "):
                    tag_akch = tag
                    in_map_akchioner(tag_akch, map_akchioner)
            print("Вроде, успешно")
            map_akchioner.update(map_fin)
            print(map_akchioner)

            return map_akchioner


# def main():
#     # KontragentParser('https://kontragent.skrin.ru/issuers/URAM').parser()
#     # k = KontragentParser("7706043263")
#     # k = KontragentParser("5053000564")
#     # k = KontragentParser('5053004833')
#     # k = KontragentParser('7707073366')
#     k = KontragentParser('7706043263')
#     a = k.parser()
#     # print(a)
#     for key in a:
#         print(key + " : " + a[key])
#
#
# if __name__ == '__main__':
#     main()
