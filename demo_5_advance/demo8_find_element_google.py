import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.google.com")

#check for presence or visiblity

print(len(driver.find_elements(By.XPATH,"//a[@id='king']")))

elements=driver.find_elements(By.XPATH,"//a")

for element in elements:
    text=element.text
    href=element.get_attribute("href")
    print(text)
    print(href)


time.sleep(5)
driver.quit()