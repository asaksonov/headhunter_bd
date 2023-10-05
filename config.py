import os.path
from configparser import ConfigParser


def config(filename="database.ini", section="postgresql"):

    # Create a parser
    parser = ConfigParser()

    if not os.path.exists(filename):
        raise FileNotFoundError

    # Read config file
    parser.read(filename)

    if parser.has_section(section):

        params = parser.items(section)
        db = dict(params)

    else:
        raise Exception(f"Section {section} is not found in the {filename} file.")

    return db



api_production_server = f'https://api.hh.ru/employers/'

companies = {'Яндекс Практикум': '5008932',
             'Skyeng': '1122462',
             'Сбербанк-Сервис': '1473866',
             'ООО Аптрейд': '10122709',
             'amoCRM': '999442',
             'ООО АВ Софт': '2355830',
             'РусЭкспресс': '1875694',
             'getmatch': '864086',
             'Точка': '10312481',
             'ScanFactory': '5580158' }

