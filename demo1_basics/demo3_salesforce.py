from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.salesforce.com/in/form/signup/freetrial-sales/")
    time.sleep(3)
    # print(driver.title)
    # driver.implicitly_wait(10)
    driver.find_element(By.NAME, "UserFirstName").send_keys("John")
    # driver.find_element("name", "username").send_keys("Admin")
    driver.implicitly_wait(10)
    driver.find_element(By.NAME, "UserLastName").send_keys("wick")
    driver.implicitly_wait(10)
    driver.find_element(By.NAME, "UserEmail").send_keys("johnwick@gmail.com")
    driver.implicitly_wait(10)
    # driver.find_element(By.NAME, "UserTitle").click()
    driver.find_element(By.XPATH, "//select[@name='UserTitle']/option[text()='IT Manager']").click()
    driver.implicitly_wait(10)

    driver.find_element(By.XPATH, "//input[@name='CompanyName']").send_keys("Pathways")
    driver.implicitly_wait(10)

    driver.find_element(By.XPATH, "//input[@name='UserPhone']").send_keys("3748223955")
    driver.implicitly_wait(10)
    # "//select[@name='element_name']/option[text()='option_text']").click()



    select_employee = Select(driver.find_element(By.XPATH, "//select[@name='CompanyEmployees']"))
    select_employee.select_by_value("250")

    select_country = Select(driver.find_element(By.XPATH, "//select[@name='CompanyCountry']"))
    select_country.select_by_visible_text("United Kingdom")

    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, "//div[@class='checkbox-ui']").click()
    driver.implicitly_wait(10)
    # driver.find_element(By.NAME, "start my free trial").click()
    driver.implicitly_wait(10)
    time.sleep(15)
    driver.quit()
