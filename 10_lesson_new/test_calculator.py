import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from calculator_page import CalculatorPage


@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Тест калькулятора с задержкой")
@allure.description("Проверяет работу калькулятора с установкой задержки и выполнением сложения")
def test_calculator():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    page = CalculatorPage(driver)

    with allure.step("Установка задержки 45 секунд"):
        page.set_delay(45)

    with allure.step("Ввод числа 7"):
        page.click_button("7")

    with allure.step("Нажатие кнопки +"):
        page.click_button("+")

    with allure.step("Ввод числа 8"):
        page.click_button("8")

    with allure.step("Нажатие кнопки ="):
        page.click_button("=")

    with allure.step("Ожидание результата и получение ответа"):
        answer = page.wait_for_result("15")

    expected_result = "15"

    @allure.step
    def check_result():
        assert answer == expected_result, f"Ожидалось {expected_result}, получено {answer}"

    check_result()

    with allure.step("Проверка успешного прохождения теста"):
        allure.attach(
            f"Тест пройден! Ожидаемый результат: {expected_result}, Фактический результат: {answer}",
            name="Результат теста",
            attachment_type=allure.attachment_type.TEXT
        )

    print("Тест пройден!")
    driver.quit()
