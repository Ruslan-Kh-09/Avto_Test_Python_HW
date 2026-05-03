from selenium import webdriver
from selenium.webdriver.common.by import By


def test_shop_total_price():
    # 1. Запуск браузера Firefox
    driver = webdriver.Firefox()
    driver.maximize_window()

    try:
        driver.get("https://www.saucedemo.com/")
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        (driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
         .click())
        driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        driver.find_element(By.ID, "checkout").click()

        driver.find_element(By.ID, "first-name").send_keys("Иван")
        driver.find_element(By.ID, "last-name").send_keys("Петров")
        driver.find_element(By.ID, "postal-code").send_keys("123456")

        driver.find_element(By.ID, "continue").click()

        total_price_element = driver.find_element(By.CLASS_NAME,
                                                  "summary_total_label")
        total_text = total_price_element.text

        assert total_text == "Total: $58.29", (f"Ожидалось $58.29,"
                                               f" но получили {total_text}")

    finally:
        driver.quit()
