import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

opt=webdriver.ChromeOptions()
opt.add_argument("--disable-notifications")
# opt.add_argument("--headless")

dic_pref={"download.default_directory":r"C:\Mine\Company\iFuture"}
opt.add_experimental_option("prefs",dic_pref)

driver=webdriver.Chrome(options=opt)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.irctc.co.in/nget/train-search")

print(driver.title)

time.sleep(5)
driver.quit()