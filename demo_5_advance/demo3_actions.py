import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://nasscom.in/")

actions = webdriver.ActionChains(driver)

actions.move_to_element(driver.find_element(By.XPATH, "//a[text()='Membership']"))\
    .perform()

#mouse hover on Become a member
actions.move_to_element(driver.find_element(By.XPATH,"//a[text()='Become a Member']")).perform()


# element is present and visible
driver.find_element(By.XPATH, "//a[text()='Membership Benefits']").click()

time.sleep(5)
driver.quit()