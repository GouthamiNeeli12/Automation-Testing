import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

service=Service(ChromeDriverManager().install())
options=webdriver.ChromeOptions()
options.add_argument('--start-maximized')
driver=webdriver.Chrome(service=service,options=options)
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.LINK_TEXT,"Shop").click()
driver.execute_script("window.scrollBy(0,500)")
ph_names=driver.find_elements(By.XPATH,"//div[@class='card h-100']")
for p in ph_names:
    if p.find_element(By.XPATH,"div/h4/a").text=="Blackberry":
        p.find_element(By.XPATH,"div/button").click()
        break
driver.execute_script("window.scrollTo(0,document.body.scrollTop)")
driver.find_element(By.XPATH,"//a[contains(text(),'Checkout')]").click()
driver.find_element(By.XPATH,"//button[normalize-space()='Checkout']").click()
driver.find_element(By.XPATH,"//input[@id='country']").send_keys("ind")
wait=WebDriverWait(driver,10)
wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@class='suggestions']/ul/li")))
eles=driver.find_elements(By.XPATH,"//div[@class='suggestions']/ul/li")
for e in eles:
    if e.text=='India':
        e.click()
        break
driver.find_element(By.CSS_SELECTOR,"label[for='checkbox2']").click()
driver.find_element(By.CSS_SELECTOR,"input[type='submit']").click()
success_text=driver.find_element(By.CLASS_NAME,"alert-success").text

assert "Success! Thank you!" in success_text

driver.close()

