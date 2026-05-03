from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_validation():

    driver = webdriver.Edge()
    driver.maximize_window()

    try:
        driver.get(" https://bonigarcia.dev/"
                   "selenium-webdriver-java/data-types.html")

        driver.find_element(By.NAME, "first-name").send_keys("Иван")
        driver.find_element(By.NAME, "last-name").send_keys("Петров")
        driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
        driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
        driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
        driver.find_element(By.NAME, "zip-code").send_keys("")
        driver.find_element(By.NAME, "city").send_keys("Москва")
        driver.find_element(By.NAME, "country").send_keys("Россия")
        driver.find_element(By.NAME, "job-position").send_keys("QA")
        driver.find_element(By.NAME, "company").send_keys("SkyPro")

        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        zip_class = (driver.find_element(By.ID, "zip-code")
                     .get_attribute("class"))
        assert "alert-danger" in zip_class

        fields = [
            "first-name", "last-name", "address", "e-mail",
            "phone", "city", "country", "job-position", "company"
        ]

        for field_id in fields:
            field_class = (driver.find_element
                           (By.ID, field_id).get_attribute("class"))
            assert "alert-success" in field_class, \
                f"Поле {field_id} должно быть зеленым"

    finally:
        driver.quit()
