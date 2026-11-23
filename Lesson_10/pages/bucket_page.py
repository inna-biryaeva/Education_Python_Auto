import allure
from selenium.webdriver.common.by import By

class BucketPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Получаем количество товаров в корзине")
    def get_count(self):
        """Возвращает количество товаров в корзине."""
        items = self.driver.find_elements(By.CLASS_NAME, "cart_item")
        return len(items)

    @allure.step("Нажимаем кнопку Checkout")
    def click_checkout(self):
        """Нажимает кнопку оформления заказа."""
        self.driver.find_element(By.ID, "checkout").click()
