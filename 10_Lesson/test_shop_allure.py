from typing import Generator
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from pages import LoginPage, InventoryPage, CartPage, CheckoutPage


@pytest.fixture
def driver() -> Generator[WebDriver, None, None]:
    """Фикстура для инициализации драйвера Chrome с
    полным отключением проверки утечки паролей."""
    options = webdriver.ChromeOptions()

    # Жестко отключаем встроенную в Chrome проверку паролей
    # на утечки и менеджер паролей
    options.add_experimental_option("prefs", {
        "profile.password_manager_leak_detection": False,
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    })

    # Блокируем стандартные уведомления браузера
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")

    # Маскируем Selenium под обычного пользователя,
    # чтобы убрать системную панику Chrome
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    options.add_argument("--disable-blink-features=AutomationControlled")

    chrome_driver: WebDriver = webdriver.Chrome(options=options)
    chrome_driver.maximize_window()

    yield chrome_driver

    chrome_driver.quit()


@allure.title("Сквозной сценарий покупки трех товаров")
@allure.description(
    "Тест проверяет полный цикл покупки: авторизацию, "
    "добавление товаров в корзину, "
    "оформление и валидацию финальной стоимости."
)
@allure.feature("Оформление заказа (Checkout)")
@allure.severity(allure.severity_level.CRITICAL)
def test_saucedemo_purchase_with_allure(driver: WebDriver) -> None:
    """Сквозной тест процесса покупки в
    магазине Saucedemo с Allure-разметкой."""
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    catalog_page = InventoryPage(driver)
    catalog_page.add_to_cart("Sauce Labs Backpack")
    catalog_page.add_to_cart("Sauce Labs Bolt T-Shirt")
    catalog_page.add_to_cart("Sauce Labs Onesie")
    catalog_page.go_to_cart()

    cart_page = CartPage(driver)
    cart_page.click_checkout()

    checkout_page = CheckoutPage(driver)
    checkout_page.fill_checkout_form("Руслан", "Хатукаев", "369000")

    total_string: str = checkout_page.get_total_price()

    with allure.step("Проверить, что итоговая сумма равна $58.29"):
        assert "$58.29" in total_string, (
            f"Ожидали сумму $58.29, но получили: {total_string}"
        )
