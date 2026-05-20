from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("http://uitestingplayground.com/ajax")

    ajax_button = driver.find_element(By.ID, "ajaxButton")
    ajax_button.click()

    wait = WebDriverWait(driver, 20)
    success_message = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "p.bg-success"))
    )

    print(success_message.text)

finally:
    driver.quit()
