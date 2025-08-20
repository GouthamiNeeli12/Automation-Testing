import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

service=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=service)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.find_element(By.XPATH,"//input[@name='name']").send_keys("Gouthami")
driver.find_element(By.XPATH,"//input[@name='email']").send_keys("gouthamin1608@gmail.com")

time.sleep(3)
driver.find_element(By.XPATH,"//input[@id='exampleInputPassword1']").send_keys("siri@1608")
driver.find_element(By.CSS_SELECTOR,"#exampleCheck1").click()

elements=Select(driver.find_element(By.CSS_SELECTOR,"#exampleFormControlSelect1"))
elements.select_by_visible_text("Male")

time.sleep(3)
driver.close()