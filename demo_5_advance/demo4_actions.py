import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://google.com/")
driver.implicitly_wait(10)

actions = webdriver.ActionChains(driver)

time.sleep(4)
actions.key_down(webdriver.Keys.SHIFT).pause(1)\
    .send_keys("hello world").key_up(webdriver.Keys.SHIFT).pause(1)\
    .send_keys(webdriver.Keys.ARROW_DOWN).pause(1).send_keys(webdriver.Keys.ARROW_DOWN).pause(1)\
    .send_keys(webdriver.Keys.ARROW_DOWN).pause(1).send_keys(webdriver.Keys.ENTER).perform().pause(1)

time.sleep(5)
driver.quit()