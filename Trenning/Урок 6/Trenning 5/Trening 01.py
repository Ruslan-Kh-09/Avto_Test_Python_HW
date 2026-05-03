from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Настройка драйвера (в данном примере Chrome)
driver = webdriver.Chrome()

try:
    # 1. Открываем сайт
    driver.get("http://the-internet.herokuapp.com")

    # 2. Настраиваем явное ожидание (Explicit Wait)
    # Ждем максимум 10 секунд, пока элемент с текстом "A/B Testing" не появится в DOM и станет видимым
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.visibility_of_element_located ((By.LINK_TEXT, "A/B Testing")))

    # 3. Проверка
    if element.is_displayed():
        print("Элемент 'A/B Testing' найден и виден на странице!")
    else:
        print("Элемент найден, но не виден.")

    sleep(5)

finally:
    # Закрываем браузер
    driver.quit()