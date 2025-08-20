from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.browserutils import Browsername


class confirm(Browsername):
    def __init__(self,driver):
        #calling the parent class by passing the driver argument
        super().__init__(driver)
        self.driver=driver
        self.checkout_url=(By.XPATH, "//button[normalize-space()='Checkout']")
        self.country=(By.XPATH, "//input[@id='country']")
        self.suggestions=(By.XPATH, "//div[@class='suggestions']/ul/li")
        self.accept_conditions=(By.CSS_SELECTOR, "label[for='checkbox2']")
        self.confirm_here=(By.CSS_SELECTOR, "input[type='submit']")

    #To handle check out page
    def checkout(self):
        self.driver.find_element(*self.checkout_url).click()
    #To handle confirmation
    def confirm(self):
        self.driver.find_element(*self.country).send_keys("ind")
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located(self.suggestions))
        eles = self.driver.find_elements(*self.suggestions)
        for e in eles:
            if e.text == 'India':
                e.click()
                break
        self.driver.find_element(*self.accept_conditions).click()
        self.driver.find_element(*self.confirm_here).click()

    #To assert the order confirmation
    def success(self):
        success_text = self.driver.find_element(By.CLASS_NAME, "alert-success").text
        return success_text
