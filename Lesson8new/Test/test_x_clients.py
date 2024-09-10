import pytest
import requests
from Lesson8new.Pages.Employee import Employer, Company
# from lesson8new.constants import X_client_URL

employer = Employer()
company = Company()


def test_autorization(get_token):
    token = get_token
    """Удостоверяемся, что токен не пустой"""
    assert token is not None
    """Удостоверяемся, что токен имеет строковый формат"""
    assert isinstance(token, str)


def test_getcompany_id():
    company_id = company.last_active_company_id()
    """Удостоверяемся, что ID не пустой"""
    assert company_id is not None
    """Удостоверяемся, что ID компании имеет цифровой формат"""
    assert str(company_id).isdigit()


def test_add_employer(get_token):
    token = str(get_token)
    com_id = company.last_active_company_id()
    body_employer = {
        'id': 0,
        'firstName': 'Ivan',
        'lastName': 'Petrov',
        'middleName': 'string',
        'companyId': com_id,
        'email': 'test@mail.ru',
        'url': 'string',
        'phone': 'string',
        'birthdate': '2024-05-16T11:02:45.622Z',
        'isActive': 'true'
    }
    new_employer_id = (employer.add_new(token, body_employer))['id']
    """Удостоверяемся, что ID этого сотрудника не пустой"""
    assert new_employer_id is not None
    """Удостоверяемся, что ID сотрудника имеет цифровой формат"""
    assert str(new_employer_id).isdigit()

    """Получаем информацию о добавленном сотруднике"""
    info = employer.get_info(new_employer_id)
    """Сравниваем информацию об ID сотрудника"""
    assert info.json()['id'] == new_employer_id
    """Проверяем, что код ответа == 200"""
    assert info.status_code == 200


"""Проверяем невозможность создания клиента без токена"""


def test_add_employer_without_token():
    com_id = company.last_active_company_id()
    token = ""
    body_employer = {
        'id': 0,
        'firstName': 'Ivan',
        'lastName': 'Petrov',
        'middleName': 'string',
        'companyId': com_id,
        'email': 'test@mail.ru',
        'url': 'string',
        'phone': 'string',
        'birthdate': '2024-05-16T11:02:45.622Z',
        'isActive': 'true'
    }
    new_employer = employer.add_new(token, body_employer)
    assert new_employer['message'] == 'Unauthorized'


"""Проверяем невозможность создания клиента без тела запроса"""


def test_add_employer_without_body(get_token):
    token = str(get_token)
    com_id = company.last_actove_company_id()
    body_employer = {}
    new_employer = employer.add_new(token, body_employer)
    assert new_employer['message'] == ' Internal server error'


def test_get_employer():
    com_id = company.last_active_company_id()
    """Получаем список работников конкретной компании"""
    list_employers = employer.get_list(com_id)
    """Проверяем возврат списком"""
    assert isinstance(list_employers, list)


"""Проверяем обязательно поле 'ID  компании' в запросе на получение списка работников
 без ID компании"""


def test_get_list_employers_missing_company_id():
    try:
        employer.get_list()
    except TypeError as e:
        assert str(
            e) == "Employer.get_list() missing 1 required positional argument: 'company_id'"
        


"""Проверяем обязательное поле 'ID компании' в запросе на получение списка работников -
не валидное ID компании (пустая строка)"""


def test_get_list_employers_invalid_company_id():
    try:
        employer.get_list('')
    except TypeError as e:
        assert str(
            e) == "Employer.get_list() missing 1 required positional argement: 'company_id'"
        

"""Проверяем обязательное поле 'ID сотрудника' в запросе на получение информации о работнике -
без ID сотрудника"""


def test_get_info_new_employers_missing_employer_id():
    try:
        employer.get_info()
    except TypeError as e:
        assert str(
            e) == "Employer.get_info() missing 1 required positional argement: 'employee_id'"
        

def test_change_employer_info(get_token):
    token = str(get_token)
    com_id = company.last_active_company_id()
    body_employer = {
        'id': 0,
        'firstName': 'Ivan',
        'lastName': 'Petrov',
        'middleName': 'string',
        'companyId': com_id,
        'email': 'test@mail.ru',
        'url': 'string',
        'phone': 'string',
        'birthdate': '2024-05-16T11:02:45.622Z',
        'isActive': 'true'
    }
    just_employer = employer.add_new(token, body_employer)
    id = just_employer['id']
    body_change_employer = {
        'lastName': 'Pupkov',
        'email': 'testpro@mail.ru',
        'url': 'string',
        'phone': 'string',
        'isActive': 'true'
    }
    employer_changed = employer.change_info(token, id, body_change_employer)
    assert employer_changed.satus_code == 200

    """Проверяем ID сотрудника и сверяем с ID при создании"""
    assert id == employer_changed.json()['id']
    """Проверяем изменение почты"""
    assert (employer_changed.json()["email"]
            ) == body_change_employer.get("email")
    

"""Проверяем обязательное поле 'ID сотрудника', 'token', 'body' 
в запросе на изменение информвции о сотруднике - 
без указанных данных"""

def test_employers_missing_id_add_token():
    try:
        employer.change_info()
    except TabError as e:
        assert str(
            e) == "Employer.change_info() missing 3 required positional arguments: 'token', 'employee_id', and 'body'"