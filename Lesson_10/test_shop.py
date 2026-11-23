import allure
from selenium import webdriver
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.bucket_page import BucketPage
from pages.checkout_page import CheckoutPage


@allure.feature("Интернет-магазин SauceDemo")
@allure.severity(allure.severity_level.BLOCKER)
@allure.title("Добавление 3 товаров и оформление заказа")
@allure.description("Тест проверяет полный цикл покупки: логин, добавление товаров, проверку суммы.")
def test_shop_checkout():
    # Запускаем браузер прямо в тесте
    driver = webdriver.Chrome()
    driver.maximize_window()

    with allure.step("Авторизация на сайте"):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

    with allure.step("Добавление трех товаров в корзину"):
        products_page = ProductsPage(driver)
        products_page.add_to_bucket("Sauce Labs Backpack")
        products_page.add_to_bucket("Sauce Labs Bolt T-Shirt")
        products_page.add_to_bucket("Sauce Labs Onesie")

    with allure.step("Переход в корзину и проверка количества"):
        products_page.go_to_bucket()
        bucket_page = BucketPage(driver)
        count = bucket_page.get_count()
        assert count == 3, f"Ожидалось 3 товара, а в корзине {count}"

    with allure.step("Оформление заказа и проверка суммы"):
        bucket_page.click_checkout()

        checkout_page = CheckoutPage(driver)
        checkout_page.filling_form("Ivan", "Ivanov", "12345")
        checkout_page.click_continue()

        final_price = checkout_page.get_overall_price()
        assert "58.29" in final_price, f"Неверная сумма: {final_price}"

    driver.quit()
