from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_slow_calculator():
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        driver.get("https://bonigarcia.dev/"
                   "selenium-webdriver-java/slow-calculator.html")

        delay_input = driver.find_element(By.ID, "delay")
        delay_input.clear()  # Очищаем поле от старого значения
        delay_input.send_keys("45")

        driver.find_element(By.XPATH, "//span[text()='7']").click()
        driver.find_element(By.XPATH, "//span[text()='+']").click()
        driver.find_element(By.XPATH, "//span[text()='8']").click()
        driver.find_element(By.XPATH, "//span[text()='=']").click()

        wait = WebDriverWait(driver, 50)
        wait.until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
        )

        result = driver.find_element(By.CLASS_NAME, "screen").text
        assert result == "15", f"Ожидалось 15, но получили {result}"

    finally:
        driver.quit()
