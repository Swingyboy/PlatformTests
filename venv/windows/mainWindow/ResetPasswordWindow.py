from selenium.webdriver.common.by import By

class ResetPassworWindow():

    def __init__(self, driver):
        self.window = driver.find_element(By.NAME, 'Reset password')

    def getTitle(self):
        return self.window.get_attribute('Name')

    def getMenuItem(self, menu, item):
        pass

    def getButton(self, button):
        return self.window.find_element(By.NAME, button)

    def setCheckbox(self, checkbox):
        self.window.find_element(By.NAME, checkbox).click()

    def close(self):
        closeButton = self.window.find_element(By.ID, 'Close')
        closeButton.click()