from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def filling_form(self, first_name, last_name, postal_code):
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)

    def click_continue(self):
        button = self.wait.until(EC.element_to_be_clickable((By.ID, "continue")))
        button.click()

    def get_overall_price(self):
        element = self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
        )
        return element.text
