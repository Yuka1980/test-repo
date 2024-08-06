from time import sleep
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://ya.ru")

element = driver.find_element(By.CSS_SELECTOR, "#text")

print(element)

# driver.find_elements()

driver.quit()