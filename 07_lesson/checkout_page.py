from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def params_user(self, first_name, last_name, postal_code):
        self.driver.find_element(
            By.CSS_SELECTOR, '[id="first-name"]').send_keys(first_name)
        self.driver.find_element(
            By.CSS_SELECTOR, '[id="last-name"]').send_keys(last_name)
        self.driver.find_element(
            By.CSS_SELECTOR, '[id="postal-code"]').send_keys(postal_code)

    def continue_button(self):
        self.wait.until(
            EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '[id="continue"]'))).click()
