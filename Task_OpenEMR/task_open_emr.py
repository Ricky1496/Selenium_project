import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


# Navigate to the demo site
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://demo.openemr.io/b/openemr/")
driver.implicitly_wait(12)

actions = webdriver.ActionChains(driver)

# Update username and password
username = driver.find_element(By.XPATH, "//input[@name='authUser']")
username.clear()
username.send_keys("admin")

password = driver.find_element(By.XPATH, "//input[@name='clearPass']")
password.clear()
password.send_keys("pass")

# Select language
language = Select(driver.find_element(By.XPATH, "//select[@name='languageChoice']"))
language.select_by_visible_text("English (Indian)")

# Click login button
login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()

# Click on Patient > New/Search

patient_menu = driver.find_element(By.XPATH, "//div[@id='menu']//li[@class='top']//a[text()='Patient']")
patient_menu.click()

new_search_option = driver.find_element(By.XPATH, "//a[text()='New/Search']")
new_search_option.click()

# Fill in patient details
first_name = driver.find_element(By.ID, "form_fname")
last_name = driver.find_element(By.ID, "form_lname")
dob = driver.find_element(By.ID, "form_DOB")
gender = Select(driver.find_element(By.XPATH, "//option[text()='Male']"))

first_name.send_keys("John")
last_name.send_keys("Doe")
dob.send_keys("02/28/2023")
gender.select_by_visible_text("Male")

# Click create new patient button
create_patient_button = driver.find_element(By.ID, "create")
create_patient_button.click()

# Wait for alert box to appear
driver.switch_to.default_content()
driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@id='modalframe']"))

driver.find_element(By.XPATH, "//input[@value='Confirm Create New Patient']").click()
driver.switch_to.default_content()
time.sleep(10)


try:
    alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
    alert_text = alert.text
    alert.accept()
    print(f"Alert box text: {alert_text}")
except TimeoutException:
    print("No alert box found.")

# Close Happy Birthday popup
try:
    happy_birthday_popup = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, "closeDlgBtn")))
    happy_birthday_popup.click()
except TimeoutException:
    print("No Happy Birthday popup found.")

# Get added patient name and print in console
added_patient_name = driver.find_element(By.XPATH, "//td[@class='patient_table_td']//a")
print(f"Added patient name: {added_patient_name.text}")

# Close the browser
driver.quit()