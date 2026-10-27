from selenium.webdriver.common.by import By

class BucketPage:
    def __init__(self, driver):
        self.driver = driver

    def get_count(self):
        items = self.driver.find_elements(By.CLASS_NAME, "cart_item")
        return len(items)

    def click_checkout(self):
        self.driver.find_element(By.ID, "checkout").click()
