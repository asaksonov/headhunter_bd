import psycopg2


class DBManager:

    def __init__(self):
        self.conn = psycopg2.connect(host='localhost', database='employers_vacancies',
                                     user='postgres', password='12345')
        self.cur = self.conn.cursor()

    def get_companies_and_vacancies_count(self):
        self.cur.execute('select name_employer, open_vacancies from employers')
        return self.cur.fetchall()

    def get_all_vacancies(self):
        self.cur.execute('select name_employer, name_vacancy, salary_from, salary_to, url_vacancy '
                    'from vacancies '
                    'inner join employers using(id_employer)'
                    )
        return self.cur.fetchall()

    def get_avg_salary(self):
        self.cur.execute('select avg(salary_from) from vacancies '
                    'where salary_from != 0')
        return self.cur.fetchall()

    def get_vacancies_with_higher_salary(self):
        self.cur.execute('select * from vacancies'
                    ' where salary_from > (select avg(salary_from)'
                    'from vacancies where salary_from != 0)')
        return self.cur.fetchall()

    def get_vacancies_with_keyword(self, word):
        self.cur.execute(f"select * from vacancies "
                    f"where name_vacancy LIKE '%{word}%'")
        return self.cur.fetchall()


db = DBManager()
try:
    with db.conn:
        print('Компания - количество открытых вакансий')
        company_quantity_vacancies = db.get_companies_and_vacancies_count()
        for el in company_quantity_vacancies:
            print(*el)

        print('Компания - вакансия')
        all_vacancies = db.get_all_vacancies()
        for el in all_vacancies:
            print(*el)

        print(f'Средняя ЗП:', round(*db.get_avg_salary()[0], 2))

        print('Вакансии с ЗП выше средней')
        for vacancy in db.get_vacancies_with_higher_salary():
            print('\n')
            for el in vacancy[1:]:
                print(el)

        print('Вакансии с поисковым словом ')
        user_word = input('Введите слово для поиска: ')
        for vacancy in db.get_vacancies_with_keyword(user_word):
            print('\n')
            for el in vacancy[1:]:
                print(el)

finally:
    db.conn.close()