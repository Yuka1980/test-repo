from selenium import webdriver
from pages.MainPage_s import MainPage
from pages.ProductPage import ProductPage
from pages.CheckoutPage import CheckoutPage
from pages.ResultPage_s import ResultPage
from pages.CartPage import CartPage
import allure


@allure.epic("Saucedemo_page_object")
@allure.severity(severity_level='normal')
@allure.title("Покупка товаров в магазине")
@allure.description("Покупка товаров в магазине, выбор определенных товаров и сравнение итоговой цены")
@allure.feature("Тест 3")
def test_buying():
    with allure.step("Логинизация на странице"):
        driver = webdriver.Chrome()
        main_page = MainPage(driver)
        main_page.open()
        main_page.user_login("standard_user")
        main_page.user_pass("secret_sauce")
        main_page.user_submit()
    with allure.step("Выбор товаров"):
        product_page = ProductPage(driver)
        added = product_page.add_to_cart()
    with allure.step("Корзина заказа"):
        cart_page = CartPage(driver)
        checkout = cart_page.checkout()
    with allure.step("Выбор оплаты"):
        checkout_page = CheckoutPage(driver)
        fill_form = checkout_page.fill_form()
    with allure.step("Страница с результатом"):
        result_page = ResultPage(driver)
    with allure.step("Сравнение стоимости заказа с ожидаемым результатом"):
        assert "Total: $58.29" == result_page.result()