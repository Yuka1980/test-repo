from selenium import webdriver 
from selenium.webdriver.common.by import By
from time import sleep

chrome = webdriver.Chrome()
firefox = webdriver.Firefox()

try:
    chrome.get("http://the-internet.herokuapp.com/add_remove_elements/")
    firefox.get("http://the-internet.herokuapp.com/add_remove_elements/")

    # нажимаем на кнопку Add Element 5 раз
    for _ in range(5):
        # add_button = chrome.find_element("xpath", "//button[text()="Add Element"]').click()
        add_button = chrome.find_element(
            By.XPATH, '//button[text()="Add Element"]').click()
        add_button = firefox.find_element(
            By.XPATH, '//button[text()="Add Element"]').click()
        sleep(1)
    # Собираем список кнопок Delete
        chrome_delete_buttons = chrome.find_elements(
            "xpath", '//button[text()="Delete"]')
        firefox_delete_buttons = firefox.find_elements(
            "xpath", '//button[text()="Delete"]')

    # Выводим размер списка на экран    
    print(
        f"Размер списка кнопок Delete в Chrome: {len(chrome_delete_buttons)}")
    print(
        f"Размер списка кнопок Delete в Firefox: {len(firefox_delete_buttons)}")