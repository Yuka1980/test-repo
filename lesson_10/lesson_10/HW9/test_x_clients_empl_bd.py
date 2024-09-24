from EmployeeApi import Employee, Company
from EmployeeTable import EmployeeTable
import allure


api = Employee("https://x-clients-be.onrender.com")
db = EmployeeTable("postgresql://x_clients_user:95PM5lQE0NfzJWDQmLjbZ45ewrz1fLYa@dpg-cqsr9ulumphs73c2q40g-a.frankfurt-postgres.render.com/x_clients_db_fxd0")

@allure.epic("X-clients")
@allure.severity(severity_level='normal')
@allure.title("Список сотрудников")
@allure.description("Получаем список сотрудников из АПИ и БД, затем сравниваем их")
@allure.feature("Тест 1")
def test_get_list_of_employers():
    with allure.step("БД - создаем компанию"):
        db.create_company("LASTONE", "Descr")
    with allure.step("БД - получаем ID последней созданной компании"):
        max_id = db.get_max_id_company()
    with allure.step("БД - добавляем сотрудника в компанию"):
        db.create_new_employee(max_id, "Name", "LastName", '+71234567890')
    with allure.step("API - получаем список сотрудников в последней созданной компании"):
        api_empl_list = api.get_list(max_id)
    with allure.step("БД - получаем список сотрудников в последней созданной компании"):
        db_empl_list = db.get_employee_list(max_id)
    with allure.step("Сравниваем список сотрудников в последней созданной компании из БД и через API"):
        assert len(db_empl_list) == len(api_empl_list)
    with allure.step("БД - получаем ID созданного сотрудника"):
        db_empl_id = db.get_max_id_employee(max_id)
    with allure.step("БД - удаляем созданного сотрудника"):
        db.delete_employee(db_empl_id)
    with allure.step("БД - удаляем созданную компанию"):
        db.delete(max_id)


@allure.epic("X-clients")
@allure.severity(severity_level='critical')
@allure.title("Добавление сотрудника")
@allure.description("Добавление сотрудника в БД и сравниваем с API: Имя, Фамилия, Телефон, Статус")
@allure.feature("Тест 2")
def test_create_new_employer():
    with allure.step("БД - создаем компанию"):
        db.create_company("LASTONE", "Descr")
    with allure.step("БД - получаем ID последней созданной компании"):
        max_id = db.get_max_id_company()
    with allure.step("API - получаем длинну списка сотрудников после создания компании"):
        api_empl_before = len(api.get_list(max_id))
    with allure.step("БД - добавляем сотрудника в компанию"):
        db.create_new_employee(max_id, "Name", "LastName", '+71234567890')
    with allure.step("БД - получаем ID созданного сотрудника"):
        db_empl_id = db.get_max_id_employee(max_id)
    with allure.step("БД - получаем длинну списка сотрудников после добавления сотрудника"):
        db_empl_list = db.get_employee_list(max_id)
    with allure.step("БД - список сотрудников не пустой"):
        assert db_empl_list is not None
    with allure.step("API - получаем длинну списка сотрудников после добавления сотрудника"):
        api_empl_after = len(api.get_list(max_id))
    with allure.step("Сравниваем список сотрудников до и после добавления сотрудника через API"):
        assert api_empl_after - api_empl_before == 1
    with allure.step("API - получаем тело списка добавленного сотрудника"):
        body = api.get_list(max_id)
    with allure.step("Проверить поля нового сотрудника. Корректно заполнены"):
        for employee in body:
            if employee["id"] == db_empl_id:
                assert employee["firstName"] == "Name"
                assert employee["lastName"] == "LastName"
                assert employee["phone"] == '+71234567890'
                assert employee["isActive"] == True
    with allure.step("БД - удаляем сотрудника из компании"):
        db.delete_employee(db_empl_id)
    with allure.step("API - получаем длинну списка сотрудников после удаления"):
        api_empl_del = len(api.get_list(max_id))
    with allure.step("Сравниваем список сотрудников до добавления и после удаления сотрудника через API"):
        assert api_empl_del == api_empl_before
    with allure.step("БД - удаляем созданную компанию"):
        db.delete(max_id)


@allure.epic("X-clients")
@allure.severity(severity_level='critical')
@allure.title("Обновление данных сотрудника")
@allure.description("Обновление данных сотрудника в БД и сравниваем с API: Имя, Фамилия, Телефон, Статус")
@allure.feature("Тест 3")
def test_update_employer():
    with allure.step("БД - создаем компанию"):
        db.create_company("LASTONE", "Descr")
    with allure.step("БД - получаем ID последней созданной компании"):
        max_id = db.get_max_id_company()
    with allure.step("БД - добавляем сотрудника в компанию"):
        db.create_new_employee(max_id, "Name", "LastName", '+71234567890')
    with allure.step("БД - получаем ID созданного сотрудника"):
        db_empl_id = db.get_max_id_employee(max_id)
    with allure.step("БД - обновление данных сотрудника в компании"):
        db.update_employee("NewName", db_empl_id)
    with allure.step("API - получаем тело списка добавленного сотрудника"):
        body = api.get_list(max_id)
    with allure.step("Проверить обновление полей нового сотрудника. Корректно заполнены"):
        for updated in body:
            if updated["id"] == db_empl_id:
                assert updated["firstName"] == "NewName"
                assert updated["lastName"] == "LastName"
                assert updated["phone"] == '+71234567890'
                assert updated["isActive"] == True
    with allure.step("БД - удаляем сотрудника из компании"):
        db.delete_employee(db_empl_id)
    with allure.step("БД - удаляем созданную компанию"):
        db.delete(max_id)


@allure.epic("X-clients")
@allure.severity(severity_level='critical')
@allure.title("Удаление сотрудника")
@allure.description("Удаление сотрудника в БД и сравниваем с API: Имя, Фамилия, Телефон, Статус")
@allure.feature("Тест 4")
def test_delete_employer():
    with allure.step("БД - создаем компанию"):
        db.create_company("LASTONE", "Descr")
    with allure.step("БД - получаем ID последней созданной компании"):
        max_id = db.get_max_id_company()
    with allure.step("БД - добавляем сотрудника в компанию"):
        db.create_new_employee(max_id, "Name", "LastName", '+71234567890')
    with allure.step("БД - получаем ID созданного сотрудника"):
        db_empl_id = db.get_max_id_employee(max_id)
    with allure.step("БД - удаляем сотрудника из компании"):
        db.delete_employee(db_empl_id)
    with allure.step("API - получаем тело списка добавленного сотрудника"):
        body = api.get_list(max_id)
    with allure.step("Сравниваем,что список сотрудников пустой через API"):
        assert body == []
    with allure.step("БД - удаляем созданную компанию"):
        db.delete(max_id)