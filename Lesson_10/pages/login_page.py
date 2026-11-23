import allure
from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открываем страницу логина")
    def open(self):
        """Открывает страницу логина."""
        self.driver.get("https://www.saucedemo.com/")

    @allure.step("Входим с логином '{username}' и паролем '{password}'")
    def login(self, username: str, password: str):
        """Заполняет форму логина и нажимает кнопку входа."""
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()
