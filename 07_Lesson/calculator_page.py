from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self._delay_input = (By.CSS_SELECTOR, "#delay")
        self._result_screen = (By.CSS_SELECTOR, ".screen")

    def open(self):
        self.driver.get("https://bonigarcia.dev/selenium-"
                        "webdriver-java/slow-calculator.html")

    def set_delay(self, seconds: str):
        delay_field = self.driver.find_element(*self._delay_input)
        delay_field.clear()
        delay_field.send_keys(seconds)

    def click_button(self, text: str):
        button_locator = (By.XPATH, f"//span[text()='{text}']")
        self.driver.find_element(*button_locator).click()

    def get_result(self, timeout: int) -> str:
        initial_text = self.driver.find_element(*self._result_screen).text

        def text_has_changed(d):
            current_text = d.find_element(*self._result_screen).text
            # Возвращаем True, когда текст перестал быть равен "7+8"
            return current_text != initial_text

        WebDriverWait(self.driver, timeout).until(text_has_changed)

        return self.driver.find_element(*self._result_screen).text
