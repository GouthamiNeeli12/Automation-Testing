from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

service=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=service)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.maximize_window()
driver.find_element(By.CSS_SELECTOR,"#name").send_keys("Rahul")
time.sleep(3)
driver.find_element(By.CSS_SELECTOR,"#alertbtn").click()
time.sleep(3)
alertbtn=driver.switch_to.alert
alertbtn.accept()
driver.close()