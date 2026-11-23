import allure
from selenium import webdriver
from pages.calc_page import CalcPage

@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Сложение двух чисел с задержкой")
@allure.description("Тест проверяет сложение 7 + 8 при задержке 45 мс.")
def test_calc_addition():
    driver = webdriver.Chrome()
    driver.maximize_window()

    with allure.step("Инициализация страницы"):
        calc_page = CalcPage(driver)

    with allure.step("Открытие страницы и установка задержки"):
        calc_page.open()
        calc_page.set_delay("45")

    with allure.step("Ввод выражения '7 + 8 ='"):
        calc_page.click_button("7")
        calc_page.click_button("+")
        calc_page.click_button("8")
        calc_page.click_button("=")

    with allure.step("Проверка результата '15'"):
        calc_page.wait_for_result("15")
        actual_result = calc_page.get_result_text()
        assert actual_result == "15", f"Ожидалось '15', получено '{actual_result}'"

    driver.quit()
