import os
from Parser_organizations.kontragent_parser import KontragentParser
from Parser_organizations.parser_data_nalog import ParserDataNalog
from Parser_organizations.rusprofile_parser import RusprofilParser
from Parser_organizations.organizations_base_data import BaseData



class Paser_all(object):

    def __init__(self, inn):
        self.inn = inn
        self.file_name = os.path.join(os.getcwd(), str(inn) + '.txt')

    # Метод для получения минимальных данных данных возврвщает словарь
    def get_map_mini_data(self):
        return ParserDataNalog(self.inn).parser_file()

    # Метод для получения расширенных данны данных возврвщает словарь
    def get_map_kontragent(self):
        map = KontragentParser(self.inn).parser()
        return map

    # Метод для данных о надежности данных возврвщает словарь
    def get_map_rusofile(self):
        map = RusprofilParser(self.inn).parsing()
        return map

    # Метод для получения всех данных возврвщает словарь
    # s
    def get_map_all(self):
        map_all = dict()
        try:
            map_all.update(self.get_map_mini_data())
        except Exception as e:
            print(str(e) + " - " + " mini_data не будет ")
        try:
            map_all.update(self.get_map_kontragent())
        except Exception as e:
            print(str(e) + " - " + "map_kontragent() не будет")
        try:
            map_all.update(self.get_map_rusofile())
        except Exception as e:
            print(str(e) + " - " + "map_rusofile() не будет")
        return map_all

    # Метод для печати выбрнных данных в файл название файла "инн".txt
    def write_data_map(self, dictionary):
        dictionary = dictionary
        print(dictionary)
        if dictionary:
            with open(self.file_name, 'a', encoding='utf-8') as ouf:
                for key in dictionary:
                    ouf.write(str(key) + ' : ' + str(dictionary[key]) + '\n')
        return dictionary

    # Метод Добавление в базу данных
    @staticmethod
    def send_base_data(dictionary):
        dictionary = dictionary
        session = BaseData.session()
        BaseData.creat_table()

        for key in dictionary:
            try:
                # print(key + " ; " + dictionary[key])
                session.add(BaseData(key, dictionary[key]))
            except:
                session.commit()

        session.commit()
        session.close()

def main():
    # dat = Paser_all('5053004833')
    # dat = Paser_all('7707073366')
    # dat =Paser_all('7710035963')
    # dat = Paser_all('7709259743')
    par = Paser_all('7839492885')
    dat =par.get_map_all()

    par.write_data_map(dat)
    Paser_all.send_base_data(dat)
    for key in dat:
        print(key + " : " + dat[key])


if __name__ == '__main__':
    main()
