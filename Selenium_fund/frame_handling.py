from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import time

service=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=service)
driver.get("https://the-internet.herokuapp.com/iframe")
driver.maximize_window()
driver.find_element(By.XPATH,"//div[@aria-label='Close']//*[name()='svg']").click()
driver.switch_to.frame('mce_0_ifr')
driver.find_element(By.TAG_NAME,"p").clear()
driver.find_element(By.TAG_NAME,"p").send_keys("Helloooooooooooo")

time.sleep(5)
