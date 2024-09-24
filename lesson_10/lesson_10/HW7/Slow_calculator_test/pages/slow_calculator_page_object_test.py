from selenium import webdriver
from pages.MainPage_c import MainPage
import allure


@allure.epic("Calculator")
@allure.severity(severity_level='normal')
@allure.title("Работа калькулятора")
@allure.description("Поиск полей, ввод данных и вывод результатов вычислений")
@allure.feature("Тест 2")
def test_calc_fill():
    driver = webdriver.Chrome()
    with allure.step("Открываем калькулятор, вводим данные, ожидаем результат"):
        main_page = MainPage(driver)
        main_page.open()
        main_page.set_delay('45')
        main_page.perform_operations()
        main_page.wait(46)
        total = main_page.total()
    with allure.step("Сравниваем результат с ожидаемым"):
        assert 15 == total