import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

# Navigate to Citibank website
driver.get("https://www.online.citibank.co.in/")

# Wait for popup to load and then close it
try:
    popup = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//a[@title='Close']"))
    )
    popup.click()
except:
    pass


# Click on Login
login_button = driver.find_element(By.XPATH, "//a[@title='LOGIN NOW']")
login_button.click()

# Click on Forgot User ID
forgot_userid_button = driver.find_element(By.XPATH, "//a[contains(text(), 'Forgot User ID?')]")
forgot_userid_button.click()

# Choose Credit Card
credit_card_button = driver.find_element(By.XPATH, "//label[@for='CreditCard']")
credit_card_button.click()

# Enter credit card number
credit_card_input = driver.find_element(By.ID, "cardNumber")
credit_card_input.send_keys("4545 5656 8887 9998")

# Enter CVV
cvv_input = driver.find_element(By.ID, "cvvNumber")
cvv_input.send_keys("123")

# Enter date
date_input = driver.find_element(By.ID, "expiryDate")
date_input.send_keys("14/04/2022")

# Click on Proceed
proceed_button = driver.find_element(By.ID, "proceed")
proceed_button.click()

# Get and print the "Please accept Terms and Conditions" text
terms_text = driver.find_element(By.XPATH, "//label[contains(text(), 'Please accept Terms and Conditions')]").text
print(terms_text)

# Quit webdriver
driver.quit()
