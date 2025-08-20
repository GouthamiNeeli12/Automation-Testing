from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

actual_list=['Cucumber - 1 Kg','Raspberry - 1/4 Kg','Strawberry - 1/4 Kg']
service=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=service)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.implicitly_wait(5)
driver.maximize_window()
driver.find_element(By.XPATH,"//input[@type='search']").send_keys("ber")
time.sleep(3)
veggies=driver.find_elements(By.XPATH,"//div[@class='products']/div/div/button")
for veg in veggies:
    veg.click()
names_list=[]
names=driver.find_elements(By.XPATH,"//h4[@class='product-name']")
for name in names:
    names_list.append(name.text)

driver.find_element(By.CSS_SELECTOR,"a[class='cart-icon']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.XPATH,"//button[text()='Apply']").click()
wait=WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))
text_found=driver.find_element(By.CSS_SELECTOR,".promoInfo").text
print(text_found)
sum=0
prices=driver.find_elements(By.CSS_SELECTOR,"tbody tr td:nth-child(5)")
for price in prices:
    sum+=int(price.text)


assert names_list==actual_list
print(sum)
total=int(driver.find_element(By.CSS_SELECTOR,".totAmt").text)
assert sum==total
disc=driver.find_element(By.CSS_SELECTOR,".discountAmt").text
assert float(disc)<total
driver.close()