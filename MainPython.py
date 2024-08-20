from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service())
driver.set_window_size(1024, 768)

print("TC1: Вход с валидными данными")

try:
    driver.get(
        "https://idemo.bspb.ru/auth?response_type=code&client_id=1&redirect_uri=https%3A%2F%2Fidemo.bspb.ru%2Flogin%2Fsuccess&prefetch_uri=https%3A%2F%2Fidemo.bspb.ru%2Flogin%2Fprefetch&force_new_session=true")
    username = driver.find_element(By.ID, "username")
    username.clear()
    username.send_keys("demo")
    password = driver.find_element(By.NAME, "password")
    password.clear()
    password.send_keys("demo")

    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)
    driver.find_element(By.ID, "login-otp-button").click()
    if driver.find_element(By.ID, "logo"): print("\033[92m{}\033[0m".format("Test PASS"))
    driver.save_screenshot("TC1_pass.png")
except:
    driver.save_screenshot("TC1_fail.png")
    print("\033[31m{}\033[0m".format("TEST FAIL"))

print("TC2: Запрет входа с невалидными учетными данными")

try:
    driver.delete_all_cookies()
    driver.get("https://idemo.bspb.ru/auth?response_type=code&client_id=1&redirect_uri=https%3A%2F%2Fidemo.bspb.ru%2Flogin%2Fsuccess&prefetch_uri=https%3A%2F%2Fidemo.bspb.ru%2Flogin%2Fprefetch&force_new_session=true")

    rand_string = ''.join(random.choice(string.ascii_lowercase) for i in range(8))
    username = driver.find_element(By.NAME, "username")
    username.clear()
    username.send_keys(rand_string)

    rand_string = ''.join(random.choice(string.ascii_lowercase) for i in range(8))
    password = driver.find_element(By.NAME, "password")
    password.clear()
    password.send_keys(rand_string)

    driver.find_element(By.ID, "login-button").click()
    if driver.find_element(By.ID, "login-button"): print ("\033[92m{}\033[0m".format("Test PASS"))
    driver.save_screenshot("screenshot_C2211.png")
except:
    driver.save_screenshot("Error_screenshot_C2211.png")
    print("\033[31m{}\033[0m".format("Test FAIL"))

driver.quit()
