from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class InventoryPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10, 0.2)


    def add_card(self, product):
        products = {
            "BACKPACK": "add-to-cart-sauce-labs-backpack",
            "BOLT_TSHIRT": "add-to-cart-sauce-labs-bolt-t-shirt",
            "ONESIE": "add-to-cart-sauce-labs-onesie"
        }

        if product in products:
            self.wait.until(
                EC.element_to_be_clickable(
                    (By.NAME, products[product]))).click()

    def go_to_cart(self):
        self.wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '.shopping - cart - link'))).click()
