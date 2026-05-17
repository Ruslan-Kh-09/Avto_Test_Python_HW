import pytest
from selenium import webdriver
from pages import LoginPage, InventoryPage, CartPage, CheckoutPage


@pytest.fixture
def driver():
    ff_driver = webdriver.Firefox()
    ff_driver.maximize_window()

    yield ff_driver

    ff_driver.quit()


def test_saucedemo_purchase(driver):
    # Авторизация
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    # Пароль secret_sauce

    # Добавление товаров в корзину
    catalog_page = InventoryPage(driver)
    catalog_page.add_to_cart("Sauce Labs Backpack")
    catalog_page.add_to_cart("Sauce Labs Bolt T-Shirt")
    catalog_page.add_to_cart("Sauce Labs Onesie")

    # Переход в корзину и клик по Checkout
    catalog_page.go_to_cart()

    cart_page = CartPage(driver)
    cart_page.click_checkout()

    # Заполнение формы заказа
    checkout_page = CheckoutPage(driver)
    checkout_page.fill_checkout_form("Руслан", "Хатукаев", "369000")

    # Получение итоговой стоимости
    total_string = checkout_page.get_total_price()

    assert "$58.29" in total_string, (
        f"Ожидали сумму $58.29, но на экране написано: '{total_string}'"
    )
