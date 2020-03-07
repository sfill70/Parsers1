
from .parser_all import Paser_all



def main():

    # inn = ['7727298791', '5047076050', '7729355029', '2130102656','7706043263', '5031078197', '6320002223', "1106014140"]

    # Сздание экземпляра класса
    # parser = Paser_all('7707073366')
    parser = Paser_all('5031078197')
    # Получение словаря со всей всей инфомацией
    data = parser.get_map_all()
    print(data)
    # Запись в файл в каталог проекта ИНН.txt
    parser.write_data_map(data)
    # Сохранение в базу данных "organization"
    # Paser_all.send_base_data(data)




if __name__ == '__main__':
    main()
