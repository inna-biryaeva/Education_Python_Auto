from selenium import webdriver

from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.bucket_page import BucketPage
from pages.checkout_page import CheckoutPage


def test_saucedemo():
    driver = webdriver.Firefox()

    login_page = LoginPage(driver)
    products_page = ProductsPage(driver)
    bucket_page = BucketPage(driver)
    checkout_page = CheckoutPage(driver)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    products_page.add_to_bucket("Sauce Labs Backpack")
    products_page.add_to_bucket("Sauce Labs Bolt T-Shirt")
    products_page.add_to_bucket("Sauce Labs Onesie")

    products_page.go_to_bucket()

    assert bucket_page.get_count() == 3

    bucket_page.click_checkout()

    checkout_page.filling_form("Иван", "Петров", "111111")
    checkout_page.click_continue()

    overall_price = checkout_page.get_overall_price()

    driver.quit()

    assert "$58.29" in overall_price
