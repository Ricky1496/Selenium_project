import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://netbanking.hdfcbank.com/netbanking/")
driver.implicitly_wait(10)

#enter user id as test123
# driver.find_element(By.XPATH, "//input[@id='liabiltyLoginCustId']").send_keys("test123")

driver.switch_to.frame(driver.find_element(By.XPATH, "//frame[@name='login_page']"))
driver.find_element(By.XPATH, "//input[@name='fldLoginUserId']").send_keys("test123")
driver.find_element(By.XPATH, "//a[@class='btn btn-primary login-btn']").click()
time.sleep(5)