from selenium.webdriver.common.by import By
import allure


class CheckoutPage:
    def __init__(self, driver):
        self._driver = driver

    @allure.step("Открываем страницу Чекаут")
    def get(self):
        self._driver.get("https://www.saucedemo.com/checkout-step-one.html")

    @allure.step("Ввод личных данных и подтверждение")
    def fill_form(self):
        self._driver.find_element(By.XPATH, '//*[@id="first-name"]').send_keys("Marina")
        self._driver.find_element(By.XPATH, '//*[@id="last-name"]').send_keys("Kanadina")
        self._driver.find_element(By.XPATH, '//*[@id="postal-code"]').send_keys("140013")
        self._driver.find_element(By.XPATH, '//*[@id="continue"]').click()