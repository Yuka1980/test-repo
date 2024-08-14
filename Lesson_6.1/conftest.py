import pytest
from selenium import webdriver # взаимодействие драйвер и браузера


@pytest.fixture()
def chrome_browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()   