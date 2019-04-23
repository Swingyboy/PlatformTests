from selenium.webdriver.common.by import By

class CopyUserSettingsWindow():

    def __init__(self, driver):
        self.window = driver.find_element(By.NAME, 'Copy user settings')

    def getTitle(self):
        return self.window.get_attribute('Name')

    def getButton(self, button):
        return self.window.find_element(By.NAME, button)

    def close(self):
        closeButton = self.window.find_element(By.ID, 'Close')
        closeButton.click()