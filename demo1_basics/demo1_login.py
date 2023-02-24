import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

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
time.sleep(2)

select_day = Select(driver.find_element(By.XPATH,"//select[@id='day']"))
select_day.select_by_value("20")
time.sleep(2)

select_month = Select(driver.find_element(By.XPATH,"//select[@id='month']"))
select_month.select_by_value("12")
time.sleep(2)

select_year = Select(driver.find_element(By.XPATH,"//select[@id='year']"))
select_year.select_by_value("1997")
time.sleep(7)
