from selenium.webdriver.common.by import By

class ExitPage():

    def __init__(self, driver):
        self.driver = driver
        self.window = self.driver.find_element(By.NAME, 'Exit')

    def clickOKbutton(self):
        OKbutton = self.window.find_element(By.NAME, 'OK')
        OKbutton.click()

    def close(self):
        self.clickOKbutton()