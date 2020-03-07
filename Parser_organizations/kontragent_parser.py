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
        url = self.url
        # url = "https://kontragent.skrin.ru/issuers/URAM"
        session = requests.Session()
        request = session.get(url, headers=headers)
        if request.status_code == 200:
            sleep(random.uniform(3, 6))
            print("ok")
            soup = BeautifulSoup(request.content, 'html.parser')

            tbody = soup.find_all('tbody')
            print('!!!!', end='Клличество tbody - ')
            print(len(tbody))

            td = tbody[len(tbody) - 1].find_all('tr')
            print(len(td))
            for tag in td:
                print()
            count = 0
            array_akchioner = []

            for tag in td:
                if not tag.is_empty_element:
                    at = re.sub(r'\n+', '\n ', str(tag.text).strip()).split('\n')
                    count = count + 1
                    array_akchioner.append([re.sub('\\s+', ' ', i) for i in at[0:len(at) + 1] if
                                            re.sub('\\s+', ' ', i) != ' ' and re.sub('\\s+', ' ', i) != ' - '])

            array_founder = []

            td1 = tbody[len(tbody) - 2].find_all('tr')
            for tag in td1:
                tr = tag.find_all('td')

                array_tr = []
                for tg in tr[1:len(tr)]:
                    at = re.sub('\\s+', ' ', str(tg.text).strip())
                    array_tr.append(at)
                if len(array_tr) > 0:
                    array_founder.append(array_tr)
                    # print(array_founder)

            array_finance_1 = []
            td2 = tbody[0]
            for tag in td2:
                try:
                    ar = re.sub(r'\\s', ' ', str(tag.text).strip()).split('\n')
                    array_finance_1.append(ar)
                except:
                    pass

            array_finanse_2 = []
            if len(tbody) > 3:
                td2 = tbody[1]
                for tag in td2:
                    try:
                        ar = re.sub(r'\\s', ' ', str(tag.text).strip()).split('\n')
                        array_finanse_2.append(ar)
                    except:
                        pass

            for i in array_finanse_2:
                for j in range(len(i)):
                    if j > 0:
                        s = "за " + str(2018 + j - len(i) + 1) + " год - " + re.sub('\\s+', ' ', str(i[j]).strip())
                        i[j] = s
                    elif j == 0:
                        s = i[j].strip().replace('\r', '')
                        i[j] = s

            dic_finanse1 = dict()
            for i in array_finance_1:
                key = ''
                volume = ''
                for j in range(len(i)):
                    if j > 0:
                        s = "за " + str(2018 + j - len(i) + 1) + " год " + re.sub('\\s+', ' ', str(i[j]).strip())
                        volume = volume + s + ', '
                    elif j == 0:
                        s = i[j].strip().replace('\r', '')
                        key = s
                dic_finanse1[key] = str(volume[0:-2])
            print("Вроде, успешно")

            akchioner = dict()
            print(array_akchioner)
            akchioner['Акционер,ИНН,Размер доли,Дата внесения'] = str(array_akchioner[::2])[1:-1].replace('\'', '')

            founder = dict()
            dic_finanse2 = dict()

            if len(array_founder[0]) > 1:
                founder['Учередитель,ИНН,Размер доли %,Сумма тыс.руб_?'] = str(array_founder)[1:-1].replace('\'', '')

            elif len(array_founder[0]) == 1:
                array_finanse_2.append('Сумма доходов')
                for i in array_founder:
                    array_finanse_2.append(i[0])
                array_founder = []
                key = ''
                volume = ''
                for j in range(len(array_finanse_2)):
                    if j > 0:
                        s = "за " + str(2018 + j - len(array_finanse_2) + 1) + " год - " + re.sub('\\s+', ' ', str(
                            array_finanse_2[j]).strip())
                        volume = volume + s + ', '
                dic_finanse2[array_finanse_2[0]] = str(volume[0:-2])

            akchioner.update(founder)
            akchioner.update(dic_finanse1)
            akchioner.update(dic_finanse2)

            return akchioner


# def main():
#     # KontragentParser('https://kontragent.skrin.ru/issuers/URAM').parser()
#     # k = KontragentParser("7706043263")
#     k = KontragentParser("5053000564")
#     # k = KontragentParser('5053004833')
#     # k = KontragentParser('7707073366')
#     # k = KontragentParser('7706043263')
#     a = k.parser()
#     print(a)
#     for key in a:
#         print(key + " : " + a[key])
#
#
# if __name__ == '__main__':
#     main()
