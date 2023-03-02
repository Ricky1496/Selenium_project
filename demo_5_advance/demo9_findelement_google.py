import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://nasscom.in/")

#presence
print(len(driver.find_elements(By.XPATH,"//a[text()='Members Listing']")))

#check for visiblity so element should be  present
print(driver.find_element(By.XPATH,"//a[text()='Members Listing']").is_displayed() )

time.sleep(5)
driver.quit()