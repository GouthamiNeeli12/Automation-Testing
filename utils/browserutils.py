#this class will be inherited by the classes that are required to print the page title.
class Browsername:
    def __init__(self, driver):
        self.driver = driver

    def getBrowserName(self):
        return self.driver.title