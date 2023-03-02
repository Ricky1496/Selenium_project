import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.google.com")

#check for presence or visiblity

#list of webelement
elements=driver.find_elements(By.XPATH,"//a")

print(len(elements))

# text=elements[0].text
# print(text)

href=elements[0].get_attribute("href")
print(href)

for i in range(0,len(elements)):
    text = elements[i].text
    print(text)
    href = elements[i].get_attribute("href")
    print(href)
    print(15*"-")


time.sleep(5)
driver.quit()