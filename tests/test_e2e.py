# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.support import expected_conditions as EC
import json

import pytest

from pageObjects.checkout_confirmation import confirm
from pageObjects.loginPage import Loginpage
from pageObjects.shopPage import shoppage
test_data_path= "C:/Users/gouth/PycharmProjects/PythonProject_selenium/data/test_e2e.json"
with open(test_data_path) as json_file:
    json_data = json.load(json_file)
    test_list=json_data["data"]

@pytest.mark.smoke
@pytest.mark.parametrize( "test_list_item", test_list )
def test_endtoend(crossbrowser,test_list_item):
    #assign the return value of crossbrowser fixture to driver
    driver=crossbrowser
    loginpage=Loginpage(driver)
    print(loginpage.getBrowserName())
    shop=loginpage.login(test_list_item["username"],test_list_item["password"])
    driver.implicitly_wait(5)
    shop.add_to_cart(test_list_item["product_name"])
    print(shop.getBrowserName())
    shop.Gotocart()
    cc=confirm(driver)
    cc.checkout()
    cc.confirm()
    text=cc.success()
    assert "Success! Thank you!" in text


