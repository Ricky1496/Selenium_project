import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.facebook.com/")
print(By.ID)
time.sleep(3)
driver.find_element(By.XPATH,"//a[normalize-space()='Create new account']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//input[@aria-label='First name']").send_keys("Ricky")
time.sleep(2)

driver.find_element(By.XPATH, "//input[@aria-label='Surname']").send_keys("Abraham")
time.sleep(5)
