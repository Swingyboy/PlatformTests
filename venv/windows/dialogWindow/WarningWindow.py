from selenium.webdriver.common.by import By

class WarningPage():

    def __init__(self, driver):
        self.driver = driver
        self.window = self.driver.find_element(By.NAME, 'Warning')

    def clickOKbutton(self):
        OKbutton = self.window.find_element(By.ID, '2')
        OKbutton.click()

    def close(self):
        self.clickOKbutton()