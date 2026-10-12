from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_session_storage_auth():
    driver = webdriver.Chrome()

    # Куки пользователя 1 (autotest30998)
    cookie_autotest30998 = {"name": "SESSION",
                    "value": "NDE0OTVhODQtYTQyNy00YWMxLTk1ZTEtY2MzNTRkNzk2ZDcy",
                    "domain": "gitflic.ru"}

    # Куки пользователя 2 (autotest5699)
    cookie_autotest5699 = {"name": "SESSION",
                    "value": "NzE5OTRiNTctNmVlNi00NGMyLWI4NzAtNGE3NzA5NjY0ZDgz",
                    "domain": "gitflic.ru"}

    # 1. Откройте страницу https://gitflic.ru/
    driver.get("https://gitflic.ru/")

    # 2. Установите cookie пользователя 1
    driver.add_cookie(cookie_autotest30998)

    # 3. Обновите страницу
    driver.refresh()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )

    # 4. Перейдите на страницу пользователя 1
    driver.get("https://gitflic.ru/user/autotest5699")

    # 5. Сохраните текущий URL
    url_autotest30998 = driver.current_url

    # 6. Разлогиньтесь (очистите куки)
    driver.delete_all_cookies()
    driver.get("https://gitflic.ru/")

    # 7. Установите cookie пользователя 2
    driver.add_cookie(cookie_autotest5699)

    # 8. Обновите страницу
    driver.refresh()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )

    # 9. Перейдите на страницу пользователя 2
    driver.get("https://gitflic.ru/user/autotest30998")

    # 10. Сохраните текущий URL
    url_autotest5699 = driver.current_url
    print("URL пользователя 2:", url_autotest5699)

    # 11. Проверьте, что URL для пользователя 1 и пользователя 2 различаются
    assert url_autotest30998 != url_autotest5699

    driver.quit()
