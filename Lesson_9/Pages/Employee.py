import requests
import json
from Lesson_9.conftest import url

path = '/employee/'

class Employer:
    def __init__(self, url=url):
        self.url = url

    # Список сотрудников компании
    def get_list(self, company_id: int):
        company = {'company': company_id}
        response = requests.get(
            self.url + '/employee', params=company)
        return response.json()
    
    # Добавление сотрудника в компанию
    def add_new(self, token: str, body: json):
        headers = {'x-client-token': token}
        response = requests.post(
            self.url + '/employee', headers=headers, json=body)
        # print(response.json())
        return response.json()
    
    # Получение информации о сотруднике
    def get_info(self, employee_id: int):
        response = requests.get(self.url + path + str(employee_id))
        return response
    
    # Изменение информации о сотруднике
    def change_info(self, token: str, employee_id: int, body: json):
        headers = {'x-client-token': token}
        response = requests.patch(self.url + path + str(employee_id), headers=headers,
                                  json=body)
        return response







class Company:
    def __init__(self, url=X_client_URL):
        self.url = url

    # Создание компании
    def create(self, token: str, body: json):
        headers = {'x-client-token': token}
        response = requests.post(
            self.url + '/company', headers=headers, params=body)
        return response.json()
    
    # Последняя созданная активная компания
    def last_active_company_id(self):
        active_params = {'active': 'true'}
        response = requests.get(
            self.url + '/company', params=active_params)
        return response.json()['id']