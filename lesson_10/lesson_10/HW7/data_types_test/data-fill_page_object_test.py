from selenium import webdriver
from pages.MainPage import MainPage
from pages.ResultPage import ResultPage
import allure


@allure.epic("Data types - registration form")
@allure.severity(severity_level='normal')
@allure.title("Заполнение формы")
@allure.description("Заполнение формы различными данными и проверка валидации данных")
@allure.feature("Тест 2")
def test_data_fill():
    driver = webdriver.Chrome()
    main_page = MainPage(driver)
    with allure.step("Переходим по ссылке заполняем поля"):
        main_page.open()
    with allure.step("Заполняем поле Имя"):
        main_page.fill_first_name("Марина")
    with allure.step("Заполняем поле Фамилия"):
        main_page.fill_last_name("Канадина")
    with allure.step("Заполняем поле Адрес"):
        main_page.fill_address("Лузянина, 2-66")
    with allure.step("Заполняем поле Индекс"):
        main_page.fill_zip_code("")
    with allure.step("Заполняем поле Город"):
        main_page.fill_city("Нижний Новгород")
    with allure.step("Заполняем поле Страна"):
        main_page.fill_country("Россия")
    with allure.step("Заполняем поле Почта"):
        main_page.fill_email("test@skypro.com")
    with allure.step("Заполняем поле Телефон"):
        main_page.fill_phone("+7985899998787")
    with allure.step("Заполняем поле Должность"):
        main_page.fill_job_position("QA")
    with allure.step("Заполняем поле Компания"):
        main_page.fill_company("SkyPro")
    with allure.step("Подтверждение данных"):
        main_page.submit()
    with allure.step("Страница с результатами"):
        result_page = ResultPage(driver)
    with allure.step("Сравниваем поле почтового индекса"):
        assert "rgba(132, 32, 41, 1)" in result_page.red_color()
    with allure.step("Сравниваем остальные поля"):
        assert "rgba(15, 81, 50, 1)" in result_page.green_color()