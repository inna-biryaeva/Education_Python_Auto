import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalcPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)

    @allure.step("Открываем страницу калькулятора")
    def open(self):
        """Открывает страницу калькулятора."""
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    @allure.step("Устанавливаем задержку: {value} мс")
    def set_delay(self, value: str):
        """Вводит значение задержки в поле и ждёт его применения."""
        delay_input = self.driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys(value)

        WebDriverWait(self.driver, 5).until(
            EC.text_to_be_present_in_element_value((By.ID, "delay"), value)
        )

    @allure.step("Нажимаем кнопку: {button_text}")
    def click_button(self, button_text: str):
        """Нажимает кнопку калькулятора."""
        button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//span[text()='{button_text}']"))
        )
        button.click()

    @allure.step("Ожидаем результат: {expected_text}")
    def wait_for_result(self, expected_text: str):
        """Ожидает появления текста на экране."""
        self.wait.until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), expected_text)
        )

    @allure.step("Получаем текст с экрана")
    def get_result_text(self):
        """Возвращает текст с экрана калькулятора."""
        element = self.driver.find_element(By.CLASS_NAME, "screen")
        return element.text
