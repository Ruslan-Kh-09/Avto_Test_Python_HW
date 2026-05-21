import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    """Класс для описания страницы авторизации интернет-магазина."""

    def __init__(self, driver: WebDriver) -> None:
        """Инициализация страницы с передачей драйвера браузера."""
        self.driver: WebDriver = driver
        self._username: tuple[str, str] = (By.CSS_SELECTOR, "#user-name")
        self._password: tuple[str, str] = (By.CSS_SELECTOR, "#password")
        self._login_btn: tuple[str, str] = (By.CSS_SELECTOR, "#login-button")

    @allure.step("Открыть главную страницу авторизации")
    def open(self) -> None:
        """Открывает веб-страницу авторизации магазина."""
        self.driver.get("https://saucedemo.com")

    @allure.step("Авторизоваться под пользователем: {user}")
    def login(self, user: str, pwd: str) -> None:
        """Вводит логин и пароль, после чего нажимает кнопку входа."""
        self.driver.find_element(*self._username).send_keys(user)
        self.driver.find_element(*self._password).send_keys(pwd)
        self.driver.find_element(*self._login_btn).click()


class InventoryPage:
    """Класс для описания главной страницы (Каталога товаров)."""

    def __init__(self, driver: WebDriver) -> None:
        """Инициализация страницы с передачей драйвера браузера."""
        self.driver: WebDriver = driver
        self._cart_icon: tuple[str, str] = (
            By.CSS_SELECTOR, ".shopping_cart_link"
        )

    @allure.step("Добавить товар '{item_name}' в корзину")
    def add_to_cart(self, item_name: str) -> None:
        """Находит кнопку добавления конкретного товара по имени и кликает."""
        xpath: str = (
            f"//div[text()='{item_name}']"
            f"/ancestor::div[@class='inventory_item']//button"
        )
        self.driver.find_element(By.XPATH, xpath).click()

    @allure.step("Перейти в корзину через верхнюю иконку")
    def go_to_cart(self) -> None:
        """Совершает переход на страницу корзины покупок."""
        self.driver.find_element(*self._cart_icon).click()


class CartPage:
    """Класс для описания страницы корзины покупателя."""

    def __init__(self, driver: WebDriver) -> None:
        """Инициализация страницы с передачей драйвера браузера."""
        self.driver: WebDriver = driver
        self._checkout_btn: tuple[str, str] = (By.CSS_SELECTOR, "#checkout")

    @allure.step("Нажать на кнопку оформления заказа (Checkout)")
    def click_checkout(self) -> None:
        """Ожидает появление кнопки Checkout
         на экране и переходит к форме заказа."""
        # Умный секундомер: ждем до 10 секунд,
        # пока кнопка станет кликабельной на экране
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self._checkout_btn)
        )
        self.driver.find_element(*self._checkout_btn).click()


class CheckoutPage:
    """Класс для описания страницы оформления и итогового расчета."""

    def __init__(self, driver: WebDriver) -> None:
        """Инициализация страницы с передачей драйвера браузера."""
        self.driver: WebDriver = driver
        self._first_name: tuple[str, str] = (By.CSS_SELECTOR, "#first-name")
        self._last_name: tuple[str, str] = (By.CSS_SELECTOR, "#last-name")
        self._postal_code: tuple[str, str] = (By.CSS_SELECTOR, "#postal-code")
        self._continue_btn: tuple[str, str] = (By.CSS_SELECTOR, "#continue")
        self._total_label: tuple[str, str] = (
            By.CSS_SELECTOR, ".summary_total_label"
        )

    @allure.step("Заполнить форму доставки данными: "
                 "{first} {last}, индекс {zip_code}")
    def fill_checkout_form(self, first: str, last: str, zip_code: str) -> None:
        """Заполняет поля имени, фамилии,
        индекса и переходит на страницу итога."""
        self.driver.find_element(*self._first_name).send_keys(first)
        self.driver.find_element(*self._last_name).send_keys(last)
        self.driver.find_element(*self._postal_code).send_keys(zip_code)
        self.driver.find_element(*self._continue_btn).click()

    @allure.step("Считать итоговую сумму заказа (Total Price)")
    def get_total_price(self) -> str:
        """Получает и возвращает текстовое значение итоговой стоимости."""
        return self.driver.find_element(*self._total_label).text
