from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from configuration import *

def test_calculator_form(chrome_browser):
    chrome_browser.get(URL_2)
    # Enter 45 in the delay input field
    delay_input = chrome_browser.find_element(By.ID, "delay")
    delay_input.clear()
    delay_input.send_keys(45)
    # Click on the buttons:
    # 7
    chrome_browser.find_element(By.XPATH, "//span[text() = '7']").click()
    # +
    chrome_browser.find_element(By.XPATH, "//span[text() = '+']").click()
    # 8
    chrome_browser.find_element(By.XPATH, "//span[text() = '8']").click()
    # =
    chrome_browser.find_element(By.XPATH, "//span[text() = '=']").click()

    # Wait for thecalculation to complete
    WebDriverWait(chrome_browser, 46).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15"))
    # Getting text_meaning from result
    result_text = chrome_browser.find_element(By.CLASS_NAME, "screen").text

    # Assert that the result is 15
    assert result_text =="15"