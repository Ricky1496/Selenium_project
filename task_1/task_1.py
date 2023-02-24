from selenium import webdriver
import time
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://github.com/login")
driver.implicitly_wait(10)
print(driver.title)
driver.find_element(By.NAME, "login").send_keys("hello")
# driver.find_element("name", "username").send_keys("Admin")
driver.implicitly_wait(10)
driver.find_element(By.NAME, "password").send_keys("89hello")
driver.implicitly_wait(10)
driver.find_element(By.NAME, "commit").click()

time.sleep(5)
driver.quit()