from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from cart_page import CartPage
from checkout_page import CheckoutPage
from inventory_page import InventoryPage
from login_page import LoginPage
from total_page import TotalPage


def test_shop():

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


    # окно регистрации
    lp = LoginPage(driver)
    lp.params_user("standard_user", "secret_sauce")
    lp.login_button()

    # окно товаров
    ip = InventoryPage(driver)
    ip.add_card("BACKPACK")
    ip.add_card("BOLT_TSHIRT")
    ip.add_card("ONESIE")
    ip.go_to_cart()

    # корзина
    cp = CartPage(driver)
    cp.click_checkout()

    # окно доставки

    chek = CheckoutPage(driver)
    chek.params_user("Джонни", "Депп", "90210")
    chek.continue_button()

    # окно суммы ( total label)
    total = TotalPage(driver)
    summ = total.result()

    # проверк, запуск теста
    assert summ == "Total: $58.29", f"результат {summ}"

    driver.quit()
