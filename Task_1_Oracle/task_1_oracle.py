from selenium import webdriver
from selenium.webdriver.common.by import By


# set up webdriver and navigate to page
driver = webdriver.Chrome()
driver.get("https://www.oracle.com/in/database/")
driver.implicitly_wait(10)

# click on View Account
view_account_button = driver.find_element(By.XPATH, "//span[@id='acctBtnLabel']")
view_account_button.click()

# click on Sign in
signin_button = driver.find_element(By.XPATH, "//a[contains(text(),'Sign-In')]")
signin_button.click()

# get and print the title and current url of the page
title = driver.title
print("Title of the page is:", title)
url = driver.current_url
print("Current URL of the page is:", url)

# get and print the page header
header = driver.find_element(By.TAG_NAME, "h1").text
print("Page header is:", header)

# enter username and password, and click on sign in
username_field = driver.find_element(By.XPATH, "//input[@name='ssousername']")
username_field.send_keys("john")

password_field = driver.find_element(By.XPATH, "//input[@name='password']")
password_field.send_keys("john123")

signin_button = driver.find_element(By.XPATH, "//input[@class='sign-in-button']")
signin_button.click()

# get and print error message
error_message = driver.find_element(By.XPATH, "//span[@class='error-show']")
print("Error message is:", error_message.text)

# close the webdriver
driver.quit()
