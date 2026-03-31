from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.driver.get("https://www.saucedemo.com/")

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#user-name"))
        )

    def params_user(self, username, password):
        username_field = self.driver.find_element(By.CSS_SELECTOR, "#user-name")
        username_field.clear()
        username_field.send_keys(username)

        password_field = self.driver.find_element(By.CSS_SELECTOR, "#password")
        password_field.clear()
        password_field.send_keys(password)

    def login_button(self):
        self.driver.find_element(By.CSS_SELECTOR, "#login-button").click()
