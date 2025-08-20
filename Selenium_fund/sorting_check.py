from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


service=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=service)
original_list=[]
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR,"th:nth-child(1)").click()
list_browser=driver.find_elements(By.CSS_SELECTOR,"tr td:nth-child(1)")
for li in list_browser:
    original_list.append(li.text)

print(original_list)
new_sorted_list=sorted(original_list)
print(new_sorted_list)
assert new_sorted_list==original_list