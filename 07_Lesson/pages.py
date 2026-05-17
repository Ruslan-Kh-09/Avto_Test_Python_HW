from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self._username = (By.CSS_SELECTOR, "#user-name")
        self._password = (By.CSS_SELECTOR, "#password")
        self._login_btn = (By.CSS_SELECTOR, "#login-button")

    def open(self):
        self.driver.get("https://www.saucedemo.com/")

    def login(self, user, pwd):
        self.driver.find_element(*self._username).send_keys(user)
        self.driver.find_element(*self._password).send_keys(pwd)
        self.driver.find_element(*self._login_btn).click()


class InventoryPage:

    def __init__(self, driver):
        self.driver = driver
        self._cart_icon = (By.CSS_SELECTOR, ".shopping_cart_link")

    def add_to_cart(self, item_name: str):
        xpath = (f"//div[text()='{item_name}']/ancestor:"
                 f":div[@class='inventory_item']//button")
        self.driver.find_element(By.XPATH, xpath).click()

    def go_to_cart(self):
        self.driver.find_element(*self._cart_icon).click()


class CartPage:

    def __init__(self, driver):
        self.driver = driver
        self._checkout_btn = (By.CSS_SELECTOR, "#checkout")

    def click_checkout(self):
        self.driver.find_element(*self._checkout_btn).click()


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self._first_name = (By.CSS_SELECTOR, "#first-name")
        self._last_name = (By.CSS_SELECTOR, "#last-name")
        self._postal_code = (By.CSS_SELECTOR, "#postal-code")
        self._continue_btn = (By.CSS_SELECTOR, "#continue")
        self._total_label = (By.CSS_SELECTOR, ".summary_total_label")

    def fill_checkout_form(self, first: str, last: str, zip_code: str):
        self.driver.find_element(*self._first_name).send_keys(first)
        self.driver.find_element(*self._last_name).send_keys(last)
        self.driver.find_element(*self._postal_code).send_keys(zip_code)
        self.driver.find_element(*self._continue_btn).click()

    def get_total_price(self) -> str:
        return self.driver.find_element(*self._total_label).text
