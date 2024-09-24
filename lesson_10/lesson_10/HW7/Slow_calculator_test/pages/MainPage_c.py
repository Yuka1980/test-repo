from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class MainPage:
    def __init__(self, driver):
        self._driver = driver

    @allure.step("Открываем страницу калькулятора")
    def open(self):
        self._driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    @allure.step("Ищем поле ввода, очищаем и вводим новое")
    def set_delay(self, term: int):
        self._driver.find_element(By.CSS_SELECTOR, "#delay").clear()
        self._driver.find_element(By.CSS_SELECTOR, "#delay").send_keys(term)

    @allure.step("Вводим значения на калькуляторе")
    def perform_operations(self):
        self._driver.find_element(By.XPATH, '//span[text() ="7"]').click()
        self._driver.find_element(By.XPATH, '//span[text() ="+"]').click()
        self._driver.find_element(By.XPATH, '//span[text() ="8"]').click()
        self._driver.find_element(By.XPATH, '//span[text() ="="]').click()

    @allure.step("Ожидаем результат вычисления")
    def wait(self, term):
        waiter = WebDriverWait(self._driver, term)
        waiter.until(
            EC.text_to_be_present_in_element((
                By.CSS_SELECTOR, 'div.screen'), "15")
            )

    @allure.step("Возвращаем полученный результат в текстовый формат")
    def total(self):
        sum = self._driver.find_element(By.CSS_SELECTOR, 'div.screen').text
        return int(sum)