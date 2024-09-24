from selenium.webdriver.common.by import By
import allure


class MainPage:
    def __init__(self, driver):
        self._driver = driver

    @allure.step("Открываем страницу для заполнения форм")
    def open(self):   
        self._driver.get("https://www.saucedemo.com/")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    @allure.step("Заполнить форму Логин")
    def user_login(self, term):
        self._driver.find_element(
            By.CSS_SELECTOR, "#user-name").send_keys(term)

    @allure.step("Заполнить форму Пароль")
    def user_pass(self, term):
        self._driver.find_element(By.CSS_SELECTOR, "#password").send_keys(term)

    @allure.step("Подтвердить введённые данные")
    def user_submit(self):
        self._driver.find_element(By.CSS_SELECTOR, "#login-button").click()