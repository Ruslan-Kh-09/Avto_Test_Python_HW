import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# 1. Указываем путь к драйверу
# Если ты положил chromedriver.exe в папку C:\, путь будет таким:
#driver_path = "C:/chromedriver.exe"

# 2. Запускаем браузер (создаем объект драйвера)
#driver = webdriver.Chrome(executable_path=driver_path)

# 3. Открываем сайт Python.org
driver.get("https://www.python.org/")
time.sleep(2)
# 4. Находим кнопку "DONATE" и нажимаем на нее
# используем поиск по тексту ссылки, так как это самый надежный способ для кнопок
# link_text находит элемент по точному тексту внутри тега <a>

#donate_button = driver.find_element(By.LINK_TEXT, "Donate")
donate_button = driver.find_element(By.CSS_SELECTOR, ".donate-button")
# donate_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".donate-button")))


donate_button.click()

# 5. Ждем пару секунд, чтобы увидеть результат
time.sleep(5)

# 6. Закрываем браузер
#driver.quit()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# # Инициализация драйвера (например, Chrome)
# driver = webdriver.Chrome()
#
# try:
#     # Переход на сайт
#     driver.get("https://python.org")
#
#     # 1. Ожидаем, пока кнопка станет кликабельной (хорошая практика)
#     wait = WebDriverWait(driver, 10)
#     donate_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".donate-button")))
#
#     # 2. Нажимаем на кнопку
#     donate_button.click()
#
#     print("Кнопка Donate успешно нажата!")
#
# finally:
#     # Закрываем браузер через пару секунд, чтобы увидеть результат
#     import time
#
#     time.sleep(3)
#     driver.quit()