from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.driver.get("https://www.saucedemo.com/")

        sleep(5)

    def params_user(self, username, password):
        self.driver.find_element(By.CSS_SELECTOR, ".user-name").send_keys(username)
        self.driver.find_element(By.CSS_SELECTOR, ".password").send_keys(password)

    def login_button(self):
        self.driver.find_element(By.CSS_SELECTOR, "login-button").click()
