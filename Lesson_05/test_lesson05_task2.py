from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/forms/post")
    driver.maximize_window()
    sleep(1)

    initial_url = driver.current_url

    name_input = driver.find_element(By.NAME, "custname")
    name_input.send_keys("Inna")
    sleep(1)

    submit_button = driver.find_element(By.XPATH, "//button[text()='Submit order']")
    submit_button.click()
    sleep(1)

    assert driver.current_url != initial_url

    driver.quit()
