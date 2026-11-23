import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    @allure.step("Заполняем форму: {first_name} {last_name}, индекс {postal_code}")
    def filling_form(self, first_name: str, last_name: str, postal_code: str):
        """Заполняет поля имени, фамилии и индексы."""
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)

    @allure.step("Нажимаем кнопку Continue")
    def click_continue(self):
        """Нажимает кнопку продолжения и ждёт перехода на страницу Overview."""
        button = self.wait.until(EC.element_to_be_clickable((By.ID, "continue")))
        button.click()

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
        )

    @allure.step("Получаем итоговую сумму")
    def get_overall_price(self):
        """Возвращает текст с итоговой суммой."""
        element = self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
        )
        return element.text
