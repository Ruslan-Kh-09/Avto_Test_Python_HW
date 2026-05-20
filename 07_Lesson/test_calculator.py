import pytest
from selenium import webdriver
from calculator_page import CalculatorPage


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.maximize_window()

    yield chrome_driver

    chrome_driver.quit()


def test_slow_calculator(driver):

    calc_page = CalculatorPage(driver)

    # 1. Открываем страницу
    calc_page.open()

    # 2. Вводим задержку 45 секунд
    calc_page.set_delay("45")

    # 3. Нажимаем последовательно кнопки
    calc_page.click_button("7")
    calc_page.click_button("+")
    calc_page.click_button("8")
    calc_page.click_button("=")

    # 4. Проверяем результат. Таймаут 50 секунд
    result = calc_page.get_result(timeout=50)

    # Финальная проверка
    assert result == "15", f"Ожидали 15, но калькулятор показал {result}"
