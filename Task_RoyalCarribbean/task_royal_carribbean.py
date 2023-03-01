import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Open the website
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.royalcaribbean.com/")
driver.implicitly_wait(10)

# Close pop-up if present
try:
    pop_up = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//div[@class='notification-banner__close']")))
    pop_up.click()
except:
    pass

driver.implicitly_wait(10)

# Click Sign in and then click Create an account
sign_in = driver.find_element(By.XPATH, "//span[contains(text(),'Sign In')]")
sign_in.click()

time.sleep(4)

create_account = driver.find_element(By.LINK_TEXT, "Create an account")
create_account.click()

time.sleep(4)

# Fill in the details
first_name = driver.find_element(By.XPATH, "//input[@id='mat-input-3']")
first_name.send_keys("Dennis")

last_name = driver.find_element(By.XPATH, "//input[@id='mat-input-4']")
last_name.send_keys("Rich")

month = driver.find_element(By.XPATH, "//span[contains(text(),'Month')]")
month.send_keys("April")

day = driver.find_element(By.XPATH, "//span[contains(text(),'Day')]")
day.send_keys("4")

year = driver.find_element(By.XPATH, "//span[contains(text(),'Year')]")
year.send_keys("1990")

country = driver.find_element(By.XPATH, "//span[contains(text(),'Country/Region of residence')]")
country.send_keys("India")

email = driver.find_element(By.XPATH, "//input[@id='mat-input-2']")
email.send_keys("example@example.com")

password = driver.find_element(By.XPATH, "//input[@id='mat-input-6']")
password.send_keys("password123")

security_question = driver.find_element(By.XPATH, "//span[contains(text(),'Select one security question')]")
security_question.send_keys("What was your first car's make or model?")

answer = driver.find_element(By.XPATH, "//input[@id='mat-input-7']")
answer.send_keys("Toyota")

terms_conditions = driver.find_element(By.XPATH, "//input[@id='mat-checkbox-3-input']")
terms_conditions.click()

done_button = driver.find_element(By.XPATH, "//button[contains(text(),'Done')]")
done_button.click()

# Close the browser
driver.quit()
