from selenium.webdriver.common.by import By
import allure


class MainPage:
    def __init__(self, driver):
        self._driver = driver

    @allure.step("Открываем страницу для заполнения форм")
    def open(self):
        self._driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    @allure.step("Ищем поле Имя для заполнения")
    def fill_first_name(self, term):
        self._driver.find_element(
            By.CSS_SELECTOR, '[name="first-name"]').send_keys(term)

    @allure.step("Ищем поле Фамилия для заполнения")
    def fill_last_name(self, term):
        self._driver.find_element(
            By.CSS_SELECTOR, '[name="last-name"]').send_keys(term)

    @allure.step("Ищем поле Адрес для заполнения")
    def fill_address(self, term):
        self._driver.find_element(
            By.CSS_SELECTOR, '[name="address"]').send_keys(term)

    @allure.step("Ищем поле Индекс для заполнения")
    def fill_zip_code(self, term):
        self._driver.find_element(
            By.CSS_SELECTOR, '[name="zip-code"]').send_keys(term)

    @allure.step("Ищем поле Город для заполнения")
    def fill_city(self, term):
        self._driver.find_element(
            By.CSS_SELECTOR, '[name="city"]').send_keys(term)

    @allure.step("Ищем поле Страна для заполнения")
    def fill_country(self, term):
        self._driver.find_element(
            By.CSS_SELECTOR, '[name="country"]').send_keys(term)

    @allure.step("Ищем поле Почта для заполнения")
    def fill_email(self, term):
        self._driver.find_element(
            By.CSS_SELECTOR, '[name="e-mail"]').send_keys(term)

    @allure.step("Ищем поле Телефон для заполнения")
    def fill_phone(self, term):
        self._driver.find_element(
            By.CSS_SELECTOR, '[name="phone"]').send_keys(term)

    @allure.step("Ищем поле Должность для заполнения")
    def fill_job_position(self, term):
        self._driver.find_element(
            By.CSS_SELECTOR, '[name="job-position"]').send_keys(term)

    @allure.step("Ищем поле Компания для заполнения")
    def fill_company(self, term):
        self._driver.find_element(
            By.CSS_SELECTOR, '[name="company"]').send_keys(term)

    @allure.step("Подтверждение данных")
    def submit(self):
        self._driver.find_element(
            By.CSS_SELECTOR, '[type="submit"]').click()