import requests
import json
import allure
x_clients_url = "https://x-clients-be.onrender.com"


class Company:
    def __init__(self, url=x_clients_url):
        self.url = url

    @allure.step("Получение ID последней активной компании")
    def last_active_company_id(self):
        active_params = {'active': 'true'}
        resp = requests.get(
            self.url + '/company', params=active_params)
        return resp.json()[-1]['id']


class Employee:
    def __init__(self, url=x_clients_url):
        self.url = url

    @allure.step("Получение списка сотрудников по ID компании")
    def get_list(self, company_id: int):
        company = {'company': company_id}
        resp = requests.get(self.url + '/employee', params=company)
        return resp.json()

    @allure.step("Добавление сотрудника в компанию")
    def add_new(self, token: str, body: json):
        headers = {'x-client-token': token}
        resp = requests.post(
            self.url + '/employee/', headers=headers, json=body)
        return resp.json()

    @allure.step("Получаем информацию о сотруднике по его ID")
    def get_info(self, employer_id: int):
        resp = requests.get(self.url + '/employee/' + str(employer_id))
        return resp

    @allure.step("Обновлем информацию о сотруднике")
    def change_info(self, token: str, employee_id: int, body: json):
        headers = {'x-client-token': token}
        resp = requests.patch(
            self.url + '/employee/' + str(employee_id), headers=headers, json=body)
        return resp