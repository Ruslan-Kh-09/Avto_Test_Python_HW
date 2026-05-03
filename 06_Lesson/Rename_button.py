from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    driver.get("http://uitestingplayground.com/textinput")

    input_field = driver.find_element(By.ID, "newButtonName")
    input_field.send_keys("SkyPro")

    update_button = driver.find_element(By.ID, "updatingButton")
    update_button.click()

    print(update_button.text)

finally:

    driver.quit()
