from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from calculator_page import CalculatorPage


def test_calculator():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    page = CalculatorPage(driver)

    page.set_delay(45)

    page.click_button("7")
    page.click_button("+")
    page.click_button("8")
    page.click_button("=")

    answer = page.wait_for_result("15")

    result = "15"

    assert result == answer, f"Ожидалось 15, получено {answer}"
    print("Тест пройден!")

    driver.quit()
