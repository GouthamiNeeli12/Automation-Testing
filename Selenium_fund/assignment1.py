from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

service=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=service)
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.implicitly_wait(5)
driver.maximize_window()

driver.find_element(By.LINK_TEXT,"Free Access to InterviewQues/ResumeAssistance/Material").click()
windows_open=driver.window_handles

driver.switch_to.window(windows_open[1])
text_toSplit=driver.find_element(By.CSS_SELECTOR,".im-para.red").text
text_splitted=text_toSplit.strip().split(" ")
for text in text_splitted:
    if '@' in text:
        txt=text
        break

driver.switch_to.window(windows_open[0])
driver.find_element(By.ID,"username").send_keys(txt)
driver.find_element(By.ID,"password").send_keys("siri1234")
driver.find_element(By.ID,"signInBtn").click()

wait=WebDriverWait(driver,5)
res=wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,".alert.alert-danger.col-md-12")))
print(res.text)