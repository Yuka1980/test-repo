from selenium.webdriver.common.by import By
import allure


class ResultPage:
    def __init__(self, driver):
        self._driver = driver

    @allure.step("Ищем поле с значением цвета: красный")
    def red_color(self):
        red_field = self._driver.find_element(
            By.CSS_SELECTOR, "div.alert-danger")
        return (
            "Value of color css property: " +
            red_field.value_of_css_property("color"))

    @allure.step("Ищем поле с значением цвета: зеленый")
    def green_color(self):
        green_field = self._driver.find_element(
            By.CSS_SELECTOR, "div.alert-success")
        return ("Value of color css property: " +
                green_field.value_of_css_property("color"))