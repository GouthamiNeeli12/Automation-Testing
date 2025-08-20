from selenium import webdriver
import time

driver=webdriver.Chrome()
driver.get("https://www.google.com")
time.sleep(3)
print(driver.title)
print(driver.current_url)