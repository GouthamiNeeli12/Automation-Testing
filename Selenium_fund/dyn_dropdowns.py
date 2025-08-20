import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=service)
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR,"#autosuggest").send_keys("ind")
time.sleep(3)
eles=driver.find_elements(By.CSS_SELECTOR,"li[class='ui-menu-item']")
#print(eles)

for ele in eles:
    if ele.text=="India":
        ele.click()

time.sleep(3)

#datePick=driver.find_element(By.XPATH,"//div[@class='ui-datepicker-header ui-widget-header ui-helper-clearfix ui-corner-left']/div[@class='ui-datepicker-title']")



print(driver.find_element(By.CSS_SELECTOR,"#autosuggest").get_attribute("value"))


