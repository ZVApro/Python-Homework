from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By


# Открыть браузер FireFox.
driver = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install()))
driver.maximize_window()

driver.get("http://the-internet.herokuapp.com/login")

search_user_name = driver.find_element(By.ID, "username")
search_user_password = driver.find_element(By.ID, "password")
click_button = driver.find_element(
    By.CSS_SELECTOR, '[type="submit"]')


search_user_name.send_keys("tomsmith")
search_user_password.send_keys("SuperSecretPassword!")
click_button.click()

green_line = driver.find_element(
    By.CSS_SELECTOR, '[class="flash success"]')
text = green_line.get_attribute("textContent").strip()
print(text[:-1])

sleep(3)

driver.quit()
