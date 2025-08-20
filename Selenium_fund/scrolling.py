from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import time

service=Service(ChromeDriverManager().install())
options=webdriver.ChromeOptions()
options.add_argument('headless')
driver=webdriver.Chrome(service=service,options=options)
driver.get("https://the-internet.herokuapp.com")
driver.maximize_window()
driver.execute_script("window.scrollBy(0,500)")
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
driver.get_screenshot_as_file("screen.png")
time.sleep(3)
