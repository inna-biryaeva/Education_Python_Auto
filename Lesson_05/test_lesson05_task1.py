from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_navigation():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online")
    driver.maximize_window()
    sleep(3)

    initial_url = driver.current_url

    driver.find_element(By.LINK_TEXT, "HTML Form").click()
    sleep(3)
    assert "/forms/post" in driver.current_url

    driver.back()
    assert initial_url == driver.current_url
    sleep(3)

    driver.quit()
