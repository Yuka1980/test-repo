from selenium.webdriver.common.by import By
import allure


class CartPage:
    def __init__(self, driver):
        self._driver = driver

    @allure.step("Открываем страницу Корзина товаров")
    def get(self):
        self._driver.get("https://www.saucedemo.com/cart.html")

    @allure.step("Подтвердить выбор")
    def checkout(self):
        self._driver.find_element(By.XPATH, '//*[@id="checkout"]').click()