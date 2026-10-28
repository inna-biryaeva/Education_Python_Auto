from selenium import webdriver
from pages.calc_page import CalcPage


def test_calc():
    driver = webdriver.Chrome()

    calc_page = CalcPage(driver)

    calc_page.open()
    calc_page.set_delay("45")

    calc_page.click_button("7")
    calc_page.click_button("+")
    calc_page.click_button("8")
    calc_page.click_button("=")

    calc_page.wait_for_result("15")

    actual_result = calc_page.get_result_text()

    assert actual_result == "15"

    driver.quit()
