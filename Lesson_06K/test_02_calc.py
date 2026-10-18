from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_slow_calculator():
    driver = webdriver.Chrome()

    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    wait = WebDriverWait(driver, 55)

    delay_input = driver.find_element(By.ID, "delay")
    delay_input.clear()
    delay_input.send_keys("45")

    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='7']"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='+']"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='8']"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='=']"))).click()

    wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15"))

    result_element = driver.find_element(By.CLASS_NAME, "screen")
    result_text = result_element.text

    assert result_text == "15"

    driver.quit()
