from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get("http://uitestingplayground.com/textinput")
search_input = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
search_input.send_keys("SkyPro")
button = driver.find_element(By.CSS_SELECTOR, "#updatingButton")
button.click()
wait = WebDriverWait(driver, 10)
wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#updatingButton"),"SkyPro"))
button_text = driver.find_element(By.CSS_SELECTOR, "#updatingButton").text
print(button_text)

driver.quit()




