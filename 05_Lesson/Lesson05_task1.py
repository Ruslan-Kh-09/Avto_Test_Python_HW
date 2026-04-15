from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager(
).install()))

driver.get("http://uitestingplayground.com/classattr/")

blue_button_locator = ("//button[contains(concat(' ',"
                       " normalize-space(@class), ' '),"
                       " ' btn-primary ')]")

wait = WebDriverWait(driver, 10)
# Разделяем аргументы на разные строки для соблюдения PEP 8
blue_button = wait.until(
    EC.element_to_be_clickable((By.XPATH, blue_button_locator))
)
blue_button.click()

wait.until(EC.alert_is_present())
alert = driver.switch_to.alert

alert.accept()

driver.quit()
