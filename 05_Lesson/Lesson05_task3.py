from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

wait = WebDriverWait(driver, 10)

try:
    driver.get("http://the-internet.herokuapp.com/inputs")

    input_field = wait.until(EC.presence_of_element_located((By.TAG_NAME,
                                                             "input")))

    input_field.send_keys("12345")
    assert input_field.get_attribute('value') == "12345"

    input_field.clear()
    assert input_field.get_attribute('value') == ""

    input_field.send_keys("54321")
    assert input_field.get_attribute('value') == "54321"

finally:
    driver.quit()
