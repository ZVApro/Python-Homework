from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def test_form():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    (driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"))

    first_name = driver.find_element(
        By.CSS_SELECTOR, '[name="first-name"]')
    first_name.send_keys("Иван")
    last_name = driver.find_element(
        By.CSS_SELECTOR, '[name="last-name"]')
    last_name.send_keys("Петров")
    address = driver.find_element(
        By.CSS_SELECTOR, '[name="address"]')
    address.send_keys("Ленина, 55-3")
    zip_code = driver.find_element(
        By.CSS_SELECTOR, '[name="zip-code"]')
    zip_code.clear()
    city = driver.find_element(
        By.CSS_SELECTOR, '[name="city"]')
    city.send_keys("Москва")
    country = driver.find_element(
        By.CSS_SELECTOR, '[name="country"]')
    country.send_keys("Россия")
    e_mail = driver.find_element(
        By.CSS_SELECTOR, '[name="e-mail"]')
    e_mail.send_keys("test@skypro.com")
    phone = driver.find_element(
        By.CSS_SELECTOR, '[name="phone"]')
    phone.send_keys("+7985899998787")
    job = driver.find_element(
        By.CSS_SELECTOR, '[name="job-position"]')
    job.send_keys("QA")
    company = driver.find_element(
        By.CSS_SELECTOR, '[name="company"]')
    company.send_keys("SkyPro")

    driver.find_element(
        By.CSS_SELECTOR, "button[type=submit]").click()

    wait = WebDriverWait(driver, 10)
    wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".alert-danger")))
    zip_code = wait.until(
        EC.presence_of_element_located((By.ID, "zip-code")))

    assert "alert-danger" in zip_code.get_attribute(
        'class'), "поле ZIP CODE не красное"

    filds_element = [
        'first-name', 'last-name', 'address', 'city', 'country',
        'e-mail', 'phone', 'job-position', 'company']
    for fild_ID in filds_element:
        fild = driver.find_element(By.ID, fild_ID)
        assert "alert-success" in fild.get_attribute(
            'class'), f"поле {fild_ID} не зелёное"

    driver.quit()
