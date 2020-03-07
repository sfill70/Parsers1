import os
import re
from Parser_organizations.receiving_data_nalog import ReceivingDataNalog


class ParserDataNalog:

    def __init__(self, inn, file='res.txt'):
        self.file = file
        self.inn = inn

    def encoding_text(self):
        global correct_encoding
        encoding = [
            'Big5'
            'utf-16',
            'utf-8',
            'GBK',
            'windows-1251',
            'ASCII',
            'US-ASCII',
            'Big5',
            'cp500',
            'cp1251'
        ]
        correct_encoding = ''
        for enc in encoding:
            try:
                open(self.file, encoding=enc).read()
            except (UnicodeDecodeError, LookupError, UnicodeError):
                pass
            else:
                correct_encoding = enc
                # print('Done!' + correct_encoding)
                break
        return correct_encoding

    def read_file(self, file, encoding):
        global text
        text = ""
        handler = open(file, 'r', encoding=encoding)
        for line in handler:
            text = text + line
        handler.close()
        return text

    def parser_file(self):
        ReceivingDataNalog(self.inn).receiving_data()
        file_for_read = os.path.join(os.getcwd(), self.file)
        correct_encoding = self.encoding_text()
        text = self.read_file(file_for_read, correct_encoding).strip()
        # print(text)
        pat_ogrn = re.compile("\\d{13}")
        pat_inn = re.compile("\\d{10}")
        pat_kpp = re.compile("\\d{9}")
        pat_dir = re.compile("((\\b([\"]?[A-ZА-Я][A-zА-я]+)\\b[\\s]{0,2}){1,3})")
        pat_data = re.compile("(\\d{2}[.]\\d{2}[.]\\d{4})")
        map = dict()
        name = re.search("!Имя!", text)
        name_org = text[0: name.start()]
        map["Название"] = name_org
        ogrn = re.search("ОГРН:", text)
        adress = text[name.end(): ogrn.start()]
        map["Адрес"] = adress.strip()
        ogrn = re.search(pat_ogrn, text[ogrn.end():len(text)])
        map["ОГРН"] = ogrn.group().strip()
        inn = re.search(pat_inn, text[re.search("ИНН:", text).end():len(text)])
        map["ИНН"] = inn.group().strip()
        kpp = re.search(pat_kpp, text[re.search("КПП:", text).end():len(text)])
        map["КПП"] = kpp.group().strip()
        try:
            dir = re.search(pat_dir, text[re.search("директор:|организация:|ПРЕЗИДЕНТ:", text, re.IGNORECASE).end():len(text)])
            # print(dir.group())
            map["Руководитель организации"] = dir.group().strip()
        except AttributeError as e:
            print("Руководитель не найден")
            print(e)
            map["Руководитель организации"] = "Не найден"
        data = re.search(pat_data, text)
        map["Дата создания (регистрации)"] = data.group().strip()
        print(map)
        print("ParserDataNalog отработал")
        return map


# def main():
#     print()
#     ParserDataNalog('5053004833').parser_file()
#
#
# if __name__ == '__main__':
#     main()
