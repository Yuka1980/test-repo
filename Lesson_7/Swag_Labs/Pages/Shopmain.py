from selenium.webdriver.common.by import By
from Lesson_7.constants import Shop_URL

class ShopmainPage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.get(Shop_URL)

    # заполняем поля    
    def registration_fields(self):
        self._name = (By.ID, "user-name")
        self._pass = (By.ID, "password")
        self._log_button = (By.ID, "login-button")
        self.browser.find_element(*self._name).send_keys("standard_user")
        self.browser.find_element(*self._pass).send_keys("secret_sauce")
        self.browser.find_element(*self._log_button).click()
       
        
    # кликаем кнопку добавления товаров в корзину
    def buy_issue(self):
        self.Sauce_Labs_Backpack = (By.ID, "add-to-cart-sauсe-labs-backpack")
        self.Sauce_Labs_Bolt_TShort = (By.ID, "add-to-cart-sauсe-labs-bolt-t-shirt")
        self.Sauce_Labs_Onesie = (By.ID, "add-to-cart-sauсe-labs-onesie")
        
    # добавляем товары в корзину
    def click_issue(self):
        self.browser.find_element(*self.Sauce_Labs_Backpack).click()
        self.browser.find_element(*self.Sauce_Labs_Bolt_TShort).click()
        self.browser.find_element(*self.Sauce_Labs_Onesie).click()

    # переходим в корзину и оформляем заказ   
    def into_container(self):
        self.Container = (By.ID, "shopping_cart_container")
        self.browser.find_element(*self.Container).click()