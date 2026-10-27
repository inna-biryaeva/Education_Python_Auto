from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalcPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 55)

    def open(self):
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def set_delay(self, value):
        delay_input = self.driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys(value)

    def click_button(self, button_text):
        button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//span[text()='{button_text}']"))
        )
        button.click()

    def wait_for_result(self, expected_text):
            self.wait.until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), expected_text)
        )

    def get_result_text(self):
        element = self.driver.find_element(By.CLASS_NAME, "screen")
        return element.text
