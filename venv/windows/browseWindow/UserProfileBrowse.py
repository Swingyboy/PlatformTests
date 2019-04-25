from selenium.webdriver.common.by import By

class UserProfileBrowse():

    def __init__(self, driver):
        self.window = driver.find_element(By.NAME, 'User Profile Manager')

    def get_title(self):
        return self.window.get_attribute('Name')

    def get_menu_item(self, menu, item):
        menuBar = self.window.find_element(By.NAME, menu)
        menuBar.click()
        return menuBar.find_element(By.NAME, item)

    def close(self):
        closeButton = self.window.find_element(By.ID, 'Close')
        closeButton.click()