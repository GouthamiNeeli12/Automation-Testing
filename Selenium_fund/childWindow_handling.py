from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


service=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=service)
driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()

driver.find_element(By.LINK_TEXT,"Click Here").click()
windows_opened=driver.window_handles
driver.switch_to.window(windows_opened[1])
print(driver.find_element(By.TAG_NAME,"h3").text)
#driver.switch_to.default_content()
driver.switch_to.window(windows_opened[0])
print(driver.find_element(By.TAG_NAME,"h3").text)