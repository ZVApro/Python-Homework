from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_calculator():

    browser = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    browser.get(
        "https://bonigarcia.dev/"
        "selenium-webdriver-java/"
        "slow-calculator.html")

    wait = WebDriverWait(browser, 45)
    delay_input = browser.find_element(By.CSS_SELECTOR, "#delay")
    delay_input.clear()
    delay_input.send_keys("45")

    browser.find_element(By.XPATH, "//span[text()='7']").click()
    browser.find_element(By.XPATH, "//span[text()='+']").click()
    browser.find_element(By.XPATH, "//span[text()='8']").click()
    browser.find_element(By.XPATH, "//span[text()='=']").click()

    wait.until(EC.text_to_be_present_in_element((
        By.CSS_SELECTOR, ".screen"), "15"))

    result = browser.find_element(By.CSS_SELECTOR, ".screen")
    total = result.get_attribute("textContent").strip()

    assert total == "15", f"результат {total}, а не 15"
