import pytest
from Lesson_9.Pages.Employee import Employer
from Lesson_9.Pages.DataBase import DataBase

api = Employer("https://x-clients-be.onrender.com")
db = DataBase(
    "postgresql+psycopg2://x_clients_user:ypYaT7FBULZv2VxrJuOHVoe78MEElWlb@dpg-crgp14o8fa8c73aritj0-a.frankfurt-postgres.render.com/x_clients_db_75hr")
# Расшифровка подключения к БД:
# - Имя пользователя: x_clients_user
# - Пароль: ypYaT7FBULZv2VxrJuOHVoe78MEElWlb
# - Хост: dpg-crgp14o8fa8c73aritj0-a.frankfurt-postgres.render.com
# - База данных: x_clients_db_75hr


# Получаем список сотрудников из БД и АПИ, после чего сравниваем их
def test_get_list_of_employers():
    # БД - Создаем компанию
    db.create_company('Evgen testers', 'cool_company')
    # БД - получаем ID последей созданной компании
    max_id = db.last_company_id()
    print(max_id)
    # БД - добавляем сотрудника в компанию
    db.create_employer(max_id, "Evgen", "Voronov", 8002000600)
    # БД - Получаем список сотрудников из последней созданной компании
    db_employer_list = db.get_list_employer(max_id)
    # API - Получаем список сотрудников из последней созданной компании
    api_employer_list = api.get_list(max_id)
    # Сравниваем список полученных сотрудников
    assert len(db_employer_list) == len(api_employer_list)
    # Удаляем сотрудника компании, в дальнейшем для удаления компании
    response = (api.get_list(max_id))[0]
    employer_id = response["id"]
    db.delete_employer(employer_id)
    # Удаляем последнюю созданную компанию
    db.delete(max_id)


# Добавляем сотрудника в БД и сравниваем с АПИ имя, фамилию, статус
def test_add_new_employer():
    db.create_company('Evgen adding new employer', 'employer')
    max_id = db.last_company_id()
    db.create_employer(max_id, "Evgen", "Voronov", 8002000600)
    response = (api.get_list(max_id))[0]
    employer_id = response["id"]
    """Сравниваем ID компании"""
    assert response["companyId"] == max_id
    """Сравниваем имя сотрудника с заданным"""
    assert response["firstName"] == "Evgen"
    """Удостоверяемся статус сострудника True"""
    assert response["isActive"] == True
    """Сравниваем фамилию сотрудника с заданной"""
    assert response["lastName"] == "Voronov"
    """БД - удаляем созданного сотрудника"""
    db.delete_employer(employer_id)
    """БД - удаляем последнюю созданную компанию"""
    db.delete(max_id)


# Сравниваем информацию о сотруднике полученную по АПИ с информацией, указанной при создании сотрудника в БД
def test_assertion_data():
    db.create_company('Employer get id company', 'new')
    max_id = db.last_company_id()
    db.create_employer(max_id, "Evgen", "Voronov", 8002000600)
    employer_id = db.get_employer_id(max_id)
    """Сравниваем информацию о сотруднике полученную по АПИ с информацтей указанной при создании сотрудника"""
    get_api_info = (api.get_info(employer_id)).json()
    assert get_api_info['firstName'] == "Evgen"
    assert get_api_info['lastName'] == "Voronov"
    assert get_api_info['phone'] == "8002000600"
    """БД - Удаляем созданного сотрудника"""
    db.delete_employer(employer_id)
    """БД - Удаляем последнюю созданную компанию"""
    db.delete(max_id)


# Сравниваем информацию о сотруднике полученную по АПИ с измененной информацией, указанной БД о сотруднике
def test_update_user_info():
    db.create_company('New updating company', 'test')
    max_id = db.last_company_id()
    db.create_employer(max_id, "Evgen", "Voronov", 8002000600)
    employer_id = db.get_employer_id(max_id)
    db.update_employer_info("King", employer_id)
    """Сравниваем информацию о сотруднике полученную по АПИ с измененной информацтей указанной при создании сотрудника"""
    get_api_info = (api.get_info(employer_id)).json()
    assert get_api_info['firstName'] == "King"
    assert get_api_info['lastName'] == "Voronov"
    assert get_api_info['isActive'] == True
    """БД - Удаляем созданного сотрудника"""
    db.delete_employer(employer_id)
    """БД - Удаляем последнюю созданную компанию"""
    db.delete(max_id)