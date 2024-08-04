from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome()
firefox = webdriver.Firefox()

try:
    # chrome.maximize_window()
    # firefox.maximize_window()
    chrome.get("http://the-internet.herokuapp.com/login")
    firefox.get("http://the-internet.herokuapp.com/login")
    input_name = chrome.find_element(By.ID, "username").send_keys("tomsmith")
    input_name = firefox.find_element(By.ID, "username").send_keys("tomsmith")
    sleep(1)
    # input_name.send_keys("tomsmith")
    input_pass = chrome.find_element(
        By.ID, "password").send_keys("SuperSecretPassword!")
    input_pass = firefox.find_element(
        By.ID, "password").send_keys("SuperSecretPassword!")
    sleep(1)
    # input_pass.send_keys("SuperSecretPassword!")
    button - chrome.find_element(By.TAG_NAME, "button").click()
    button - firefox.find_element(By.TAG_NAME, "button").click()
    sleep(2)
    
except Exception as ex:
    print(ex)
finally:
    chrome.quit()
    firefox.quit()