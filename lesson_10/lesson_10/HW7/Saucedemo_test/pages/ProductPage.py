from selenium.webdriver.common.by import By
import allure


class ProductPage:
    def __init__(self, driver):
        self._driver = driver

    @allure.step("Выбор товаров и подтверждение заказа")
    def add_to_cart(self):
        self._driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]').click()
        self._driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
        self._driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-onesie"]').click()
        self._driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()