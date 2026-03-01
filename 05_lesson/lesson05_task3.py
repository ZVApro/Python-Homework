from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

# Открыть браузер FireFox.
driver = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install()))
driver.maximize_window()

driver.get("http://the-internet.herokuapp.com/inputs")

search_input = driver.find_element(
    By.CSS_SELECTOR, "input[type='number']")
search_input.send_keys("Sky")
sleep(10)
search_input.clear()

search_input.send_keys("Pro")

sleep(10)
driver.quit()
