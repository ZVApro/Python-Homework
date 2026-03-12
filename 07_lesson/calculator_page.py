from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class CalculatorPage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def set_delay(self, seconds):
        delay = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay.clear()
        delay.send_keys(str(seconds))

    def click_button(self, text):
        self.driver.find_element(By.XPATH, f"//span[text()='{text}']").click()

    def wait_for_result(self, expected):
        wait = WebDriverWait(self.driver, 45, 0.2)
        screen = self.driver.find_element(By.CSS_SELECTOR, ".screen")
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), str(expected)))

        result = screen.get_attribute("textContent").strip()
        return result
