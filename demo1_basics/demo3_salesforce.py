from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.salesforce.com/in/form/signup/freetrial-sales/")
    driver.implicitly_wait(10)
    time.sleep(3)

    driver.find_element(By.NAME, "UserFirstName").send_keys("John")

    driver.find_element(By.NAME, "UserLastName").send_keys("wick")

    driver.find_element(By.NAME, "UserEmail").send_keys("johnwick@gmail.com")

    select_job_title = Select(driver.find_element(By.XPATH, "//select[@name='UserTitle']"))
    select_job_title.select_by_visible_text("IT Manager")

    # driver.find_element(By.XPATH, "//input[@name='CompanyName']").send_keys("Pathways")

    error = driver.find_element(By.XPATH, "span[contains(@id='CompanyName-fsJj-errMsg')]").text()
    print(error)
    driver.find_element(By.XPATH, "//input[@name='UserPhone']").send_keys("3748223955")

    select_employee = Select(driver.find_element(By.XPATH, "//select[@name='CompanyEmployees']"))
    select_employee.select_by_value("250")

    select_country = Select(driver.find_element(By.XPATH, "//select[@name='CompanyCountry']"))
    select_country.select_by_visible_text("United Kingdom")

    driver.find_element(By.XPATH, "//div[@class='checkbox-ui']").click()

    # driver.find_element(By.NAME, "start my free trial").click()
    time.sleep(9)
    driver.quit()
