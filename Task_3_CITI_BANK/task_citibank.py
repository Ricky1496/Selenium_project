import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
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

driver.switch_to.window(driver.window_handles[1])
# Click on Forgot User ID
forgot_userid_button = driver.find_element(By.XPATH, "//div[contains(text(),'Forgot User ID?')]")
forgot_userid_button.click()

#toggle
driver.find_element(By.XPATH, "//a[@class='sbToggle']").click()

# Choose Credit Card
credit_card_button = driver.find_element(By.XPATH, "//a[@rel='Credit Card']")
credit_card_button.click()

# Enter credit card number
credit_card_1_input = driver.find_element(By.XPATH, "//input[@id='citiCard1']")
credit_card_1_input.send_keys("4545")

credit_card_2_input = driver.find_element(By.XPATH, "//input[@id='citiCard2']")
credit_card_2_input.send_keys("5656")

credit_card_3_input = driver.find_element(By.XPATH, "//input[@id='citiCard3']")
credit_card_3_input.send_keys("8887")

credit_card_4_input = driver.find_element(By.XPATH, "//input[@id='citiCard4']")
credit_card_4_input.send_keys("9998")

# Enter CVV
cvv_input = driver.find_element(By.XPATH, "//input[@id='cvvnumber']")
cvv_input.send_keys("123")

# Enter date
driver.find_element(By.XPATH, "//input[@id='bill-date-long']").click()
Select(driver.find_element(By.XPATH, "//select[@class='ui-datepicker-year']")).select_by_value('2022')
Select(driver.find_element(By.XPATH, "//select[@class='ui-datepicker-month']")).select_by_visible_text('Apr')
driver.find_element(By.LINK_TEXT, "14").click()

# Click on Proceed
proceed_button = driver.find_element(By.XPATH, "//input[@value='PROCEED']")
proceed_button.click()

# Get and print the "Please accept Terms and Conditions" text
error_message = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/li").text
print("Error Message: ", error_message)

time.sleep(5)

# Quit webdriver
driver.quit()
