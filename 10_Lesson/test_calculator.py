import allure
import pytest
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from calculator_page import CalculatorPage


@pytest.fixture
def driver() -> WebDriver:
    """Фикстура для создания, настройки и закрытия драйвера Chrome."""
    options = webdriver.ChromeOptions()
    chrome_driver: WebDriver = webdriver.Chrome(options=options)
    chrome_driver.maximize_window()

    yield chrome_driver

    chrome_driver.quit()


@allure.title("Проверка работы калькулятора с задержкой")
@allure.description(
    "Тест вводит задержку в 45 секунд, выполняет сложение 7 + 8 "
    "и дожидается появления корректного результата '15' на экране."
)
@allure.feature("Математические вычисления")
@allure.severity(allure.severity_level.NORMAL)
def test_slow_calculator(driver: WebDriver) -> None:
    """Автотест для верификации вычислений калькулятора с таймаутом."""
    calc_page = CalculatorPage(driver)

    calc_page.open()
    calc_page.set_delay("45")

    calc_page.click_button("7")
    calc_page.click_button("+")
    calc_page.click_button("8")
    calc_page.click_button("=")

    result: str = calc_page.get_result(timeout=50)

    with allure.step("Проверить, что итоговый результат на экране равен 15"):
        assert result == "15", (
            f"Ожидали 15, но калькулятор показал {result}"
        )
