from selenium.webdriver.common.by import By

from pageObjects.shopPage import shoppage
from utils.browserutils import Browsername


#below class is inheriting Browsername class functionalities to work on it's methods
class Loginpage(Browsername):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver
        self.username_input=(By.CSS_SELECTOR, "#username")
        self.password_input=(By.ID, "password")

    #Login page is handled here
    def login(self,username,password):
        self.driver.get("https://rahulshettyacademy.com/loginpagePractise/")
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, "#signInBtn").click()
        shop = shoppage(self.driver)
        return shop
