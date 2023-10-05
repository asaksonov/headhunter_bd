import requests


class HH_parser:

    def __init__(self, api_production_server):
        self.api_production_server = api_production_server
        print(self.api_production_server)

    def get_company(self, id_company):
        params = {'area': 113,
                  'locale': 'RU',
                  'only_with_vacancies': True, }
        response = requests.get(f'{self.api_production_server}{id_company}', params=params)
        if response.status_code == 200:
            return response
        return quit('Ошибка запроса!')

    def get_vacancies(self, vacancies_url, page=0):
        params = {
            'page': page,
            'per_page': 100
        }
        response = requests.get(vacancies_url, params=params)
        if response.status_code == 200:
            return response
        return quit('Ошибка запроса!')
