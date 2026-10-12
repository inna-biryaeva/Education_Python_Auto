from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_loading():
    driver = webdriver.Chrome()

    # 1. Откройте страницу
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

    # 2. Найдите и нажмите на кнопку "Start"
    start_button = WebDriverWait(driver,20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Start']"))
        )
    start_button.click()

    # 3. Дождитесь появления текста "Hello World!"
    final_text = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, '//h4[text() = "Hello World!"]'))
    )

    # 4. Сделайте скриншот страницы
    driver.save_screenshot('screenshorts/screenshot1.png')


    # 5. Проверьте, что появившийся текст равен "Hello World!"
    actual_text = final_text.text
    assert actual_text == "Hello World!"

    driver.quit()
