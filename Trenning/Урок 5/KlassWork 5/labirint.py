from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
#from selenium.webdriver.common.devtools.v145.dom import discard_search_results
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

# Надо зайти на лабиринт
driver.get('https://www.labirint.ru')

# Найти книги по слову Python
#search_locator = "#search-field"
#search_input = driver.find_element(By.CSS_SELECTOR, search_locator)
search_input = driver.find_element(By.CSS_SELECTOR, "#search-field")
search_input.send_keys("Python", Keys.RETURN)

#search_input.send_keys(Keys.ENTER)

# Собрать все карточки товаров
book_locator = "div.product"

books = driver.find_elements(By.CSS_SELECTOR, "div.product")

# Вывести в консоль инфу: Название, цена, автор

# for book in books:
#     author = ''
#     try:
#         author = book.find_element(By.CSS_SELECTOR, 'div.product-author')
#     except:
#         author = "Автор не указан!"
#
#     print(author)

for book in books:
	author = " " #ожидается ошибка, поэтому значение переменной пока не определяем
	try: #Python сам попробует определить значение
		author = book.find_element(By.CSS_SELECTOR, "div.product-card__author").text
	except: #если не получится, то значение мы задали сами
		author = "Автор не указан"

	print(author)

sleep(1)
