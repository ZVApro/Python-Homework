from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def test_shop():
    browser = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    browser.implicitly_wait(10)
    wait = WebDriverWait(browser, 10)
    browser.get("https://www.saucedemo.com/")

    browser.find_element(
        By.CSS_SELECTOR, ".user-name").send_keys('standard_user')
    browser.find_element(
        By.CSS_SELECTOR, ".password").send_keys('secret_sauce')
    browser.find_element(
        By.CSS_SELECTOR, "login-button").click()

    wait.until(
        EC.element_to_be_clickable((
            By.CSS_SELECTOR,
            '[id="add-to-cart-sauce-labs-backpack"]'))).click()
    wait.until(
        EC.element_to_be_clickable((
            By.CSS_SELECTOR,
            '[id="add-to-cart-sauce-labs-bolt-t-shirt"]'))).click()
    wait.until(
        EC.element_to_be_clickable((
            By.CSS_SELECTOR,
            '[id="add-to-cart-sauce-labs-onesie"]'))).click()
    wait.until(
        EC.element_to_be_clickable((
            By.CSS_SELECTOR, '.shopping - cart - link'))).click()

    wait.until(EC.element_to_be_clickable((
        By.CSS_SELECTOR, '[id="checkout"]'))).click()

    browser.find_element(
        By.CSS_SELECTOR, '[id="first-name"]').send_keys('Джонни')
    browser.find_element(
        By.CSS_SELECTOR, '[id="last-name"]').send_keys('Депп')
    browser.find_element(
        By.CSS_SELECTOR, '[id="postal-code"]').send_keys('6200778')
    wait.until(EC.element_to_be_clickable((
        By.CSS_SELECTOR, '[id="continue"]'))).click()

    result = wait.until(EC.presence_of_element_located((
        By.CSS_SELECTOR, '[class="summary_total_label"]')))
    total = result.get_attribute("textContent").strip()

    assert total == "Total: $58.29", f"результат {total}"

    browser.quit()
