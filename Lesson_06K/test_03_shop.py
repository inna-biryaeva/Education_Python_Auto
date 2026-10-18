from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_saucedemo_purchase():
    driver = webdriver.Firefox()

    driver.get("https://www.saucedemo.com/")
    wait = WebDriverWait(driver, 15)

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_item")))

    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()

    driver.find_element(By.ID, "first-name").send_keys("Inna")
    driver.find_element(By.ID, "last-name").send_keys("Biriaeva")
    driver.find_element(By.ID, "postal-code").send_keys("127101")

    driver.find_element(By.ID, "continue").click()

    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label")))
    overall_text = driver.find_element(By.CLASS_NAME, "summary_total_label").text

    driver.quit()

    assert "$58.29" in overall_text
