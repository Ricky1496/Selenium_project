from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# set the path of the webdriver
driver = webdriver.Chrome()

# navigate to the Oracle login page
driver.get("https://www.oracle.com/index.html")

# click on the 'Sign In' link
sign_in_link = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.LINK_TEXT, "Sign In")))
sign_in_link.click()

# switch to the login iframe
driver.switch_to.frame("idcs-signin-widget")

# enter the login credentials
username_field = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "userNameInput")))
username_field.send_keys("your_username")
password_field = driver.find_element_by_id("passwordInputField")
password_field.send_keys("your_password")
sign_in_button = driver.find_element_by_id("submitButton")
sign_in_button.click()

# wait for the 'View Account' button to load and click it
view_account_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//a[@title='View Account']")))
view_account_button.click()

# quit the browser window
driver.quit()
