Класс для работы с парсерами
parser_all класс Parser_all
создать экземпляр класса, прердать ему исходные данные (ИНН, ОГРН) -  Parser_all (ИНН)

Parser_all(ИНН).get_map_mini_data - Метод для получения
                                     минимальных данных данных возврвщает словарь String : String

Parser_all(ИНН).get_map_kontragent(self) - Метод для получения расширенных данны
                                           данных возврвщает словарь String : String

Parser_all(ИНН).get_map_rusofile  - Метод для данных о надежности и судебных производствах (если есть) организаии данных
                                    возврвщает словарь String : String


Paser_all.write_data_map(self, dictionary) - Метод для печати выбрнных данных в файл принимает
                                       экземпляр класса и словарь поученный однимиз методо от этого
                                       экземпляра

Paser_all.send_base_data(self, dictionary) - Метод для передачи выбрнных данных в базу данных принимает
                                      словарь поученный одним из методо от этого
                                       экземпляра


Пример:

 # Сздание экземпляра класса
    parser = Paser_all('7709259743')
    # Получение словаря со всей всей инфомацией
    dictionary = parser.get_map_all()
    # Получение словаря со краткой инфомацией
    dictionary1 = parser.get_map_mini_data
    # Получение словаря со краткой инфомацией
    dictionary2 = parser.get_map_kontragent
    #Получения словаря о надежности
    dictionary3 = parser.get_map_rusofile

    # Запись в файл в каталог проекта ИНН.txt
    Paser_all(ИНН).write_data_map(dictionary)
    Paser_all.write_data_map(parser, dictionary)
    # Запись в базу данных
    Paser_all.send_base_data(dictionary)




kontragent_get_url.py получает url по ИНН с сайта
https://kontragent.skrin.ru/
kontragent_parser.py парсит эти данные возврашает словарь String : String


receiving_data_nalog.py получает краткие данные фирмы по ИНН с сайта
https://egrul.nalog.ru/index.html
получет выписку в текущую деректорию
parser_data_nalog.py парсит файл возврашает словарь String : String

rusofile_parser.py
получает даные о надежности и судебных производствах (если есть )оганизации возврашает словарь String : String
