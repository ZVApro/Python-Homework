import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from cart_page import CartPage
from checkout_page import CheckoutPage
from inventory_page import InventoryPage
from login_page import LoginPage
from total_page import TotalPage


@allure.feature("Покупка товаров")
@allure.severity(allure.severity_level.BLOCKER)
@allure.title("Полный сценарий покупки товаров")
@allure.description("Проходит полный путь от входа в систему до оформления заказа с проверкой итоговой суммы")
def test_shop():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    with allure.step("Вход в систему"):
        lp = LoginPage(driver)
        lp.params_user("standard_user", "secret_sauce")
        lp.login_button()

    with allure.step("Добавление товаров в корзину"):
        ip = InventoryPage(driver)
        ip.add_card("BACKPACK")
        ip.add_card("BOLT_TSHIRT")
        ip.add_card("ONESIE")
        ip.go_to_cart()

    with allure.step("Переход к оформлению заказа"):
        cp = CartPage(driver)
        cp.click_checkout()

    with allure.step("Заполнение данных пользователя"):
        chek = CheckoutPage(driver)
        chek.params_user("Джонни", "Депп", "90210")
        chek.continue_button()

    with allure.step("Получение итоговой суммы"):
        total = TotalPage(driver)
        summ = total.result()

    expected_total = "Total: $58.29"

    @allure.step
    def check_total_amount():
        assert summ == expected_total, f"Результат {summ}"

    check_total_amount()

    with allure.step("Подтверждение успешного прохождения теста"):
        allure.attach(
            f"Итоговая сумма корректна: {summ}",
            name="Результат проверки суммы",
            attachment_type=allure.attachment_type.TEXT
        )

    driver.quit()
