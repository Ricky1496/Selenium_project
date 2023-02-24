from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.db4free.net/")
    driver.implicitly_wait(10)

    driver.find_element(By.LINK_TEXT, "phpMyAdmin »").click()
    driver.switch_to.window(driver.window_handles[1])

    driver.find_element(By.XPATH, "//input[@name='pma_username']").send_keys("sd")
    driver.find_element(By.XPATH, "//input[@name='pma_password']").send_keys("sd")

    time.sleep(3)
    driver.find_element(By.XPATH, "//input[@class='btn btn-primary']").click()

    driver.close()

    time.sleep(5)