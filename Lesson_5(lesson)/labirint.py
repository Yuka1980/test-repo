

from time import sleep
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()


# зайти на сайт лабиринт
driver.get("https://www.labirint.ru")

# отсортировать книги по слову Python
search_field = "#search-field"
search_input = driver.find_element(By.CSS_SELECTOR, search_field)
search_input.send_keys("Python")
search_input.send_keys(Keys.ENTER)

# собрать все карточки товаров
books = driver.find_elements(By.CSS_SELECTOR, "div.product-card")

print(len(books))


# вывести в консоль информацию название + автор + цена

for book in books:
    title = book.find_element(By.CSS_SELECTOR, "a.product-card_name").text
    price = book.find_element(By.CSS_SELECTOR, "div.product-card_price-current").text 
    autor = " "
    try:
        autor = book.find_element(By.CSS_SELECTOR, "div.product-card_autor").text
    except:
        autor = "Автор не указан"

    print(len(books))

   
   

# $$("span.price-val")
# $$("product-title")


sleep(5)