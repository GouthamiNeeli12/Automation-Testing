from selenium.webdriver.common.by import By

from utils.browserutils import Browsername


class shoppage(Browsername):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.shop_link=(By.LINK_TEXT, "Shop")
        self.product_list=(By.XPATH, "//div[@class='card h-100']")
        self.check_out_button=(By.XPATH, "//a[contains(text(),'Checkout')]")

    def add_to_cart(self,product_name):
        self.driver.find_element(*self.shop_link).click()
        self.driver.execute_script("window.scrollBy(0,500)")
        ph_names = self.driver.find_elements(*self.product_list)
        for p in ph_names:
            if p.find_element(By.XPATH, "div/h4/a").text == product_name:
                p.find_element(By.XPATH, "div/button").click()
                break
        self.driver.execute_script("window.scrollTo(0,document.body.scrollTop)")

    def Gotocart(self):
        self.driver.find_element(*self.check_out_button).click()
