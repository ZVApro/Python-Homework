from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class TotalPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10, 0.2)
        self.total = None

    def result(self):
        result = self.wait.until(EC.presence_of_element_located((
            By.CSS_SELECTOR, '[class="summary_total_label"]')))
        total = result.get_attribute("textContent").strip()
        return total
