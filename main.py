from api_hh import HH_parser
from config import *
from database import DataBase


api_hh = HH_parser(api_production_server)
database = DataBase()
params = config()

try:
    with database.conn:

        database.create_table_vacancies()
        database.create_table_employers()
        for id_company in companies:
            company = api_hh.get_company(id_company=companies[id_company]).json()
            write_to_basedate_emp = database.writing_data_to_table_employers(company)

            vacancies_url = company['vacancies_url']
            pages = api_hh.get_vacancies(vacancies_url, 0).json()['pages']
            for page in range(pages):
                vacancies = api_hh.get_vacancies(vacancies_url, page).json()
                for vacancy in vacancies['items']:
                    write_to_basedate_vac = database.writing_data_to_table_vacancies(vacancy)

finally:
    database.conn.close()


