import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class CalculatorPage:
    """Класс для взаимодействия со страницей медленного калькулятора."""

    def __init__(self, driver: WebDriver) -> None:
        """Инициализация страницы с передачей драйвера браузера."""
        self.driver: WebDriver = driver
        self._delay_input: tuple[str, str] = (By.CSS_SELECTOR, "#delay")
        self._result_screen: tuple[str, str] = (By.CSS_SELECTOR, ".screen")

    @allure.step("Открыть страницу медленного калькулятора")
    def open(self) -> None:
        """Открывает веб-страницу калькулятора."""
        self.driver.get(
            "https://bonigarcia.dev"
        )

    @allure.step("Установить задержку вычислений в {seconds} секунд(ы)")
    def set_delay(self, seconds: str) -> None:
        """Очищает поле задержки и вводит новое текстовое значение."""
        delay_field: WebElement = self.driver.find_element(*self._delay_input)
        delay_field.clear()
        delay_field.send_keys(seconds)

    @allure.step("Нажать на кнопку калькулятора: {text}")
    def click_button(self, text: str) -> None:
        """Находит кнопку калькулятора по её тексту и совершает клик."""
        button_locator: tuple[str, str] = (
            By.XPATH, f"//span[text()='{text}']"
        )
        self.driver.find_element(*button_locator).click()

    @allure.step("Ожидать и получить финальный результат вычислений")
    def get_result(self, timeout: int) -> str:
        """Ожидает, пока выражение на экране сменится итоговым результатом."""
        initial_text: str = self.driver.find_element(*self._result_screen).text

        def text_has_changed(d: WebDriver) -> bool:
            """Внутренняя функция для проверки изменения текста на экране."""
            current_text: str = d.find_element(*self._result_screen).text
            return current_text != initial_text

        WebDriverWait(self.driver, timeout).until(text_has_changed)

        return self.driver.find_element(*self._result_screen).text
