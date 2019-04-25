from selenium.webdriver.common.by import By

class ResetPassworWindow():

    def __init__(self, driver):
        self.window = driver.find_element(By.NAME, 'Reset password')

    def get_title(self):
        return self.window.get_attribute('Name')

    def get_menu_item(self, menu, item):
        pass

    def get_button(self, button):
        return self.window.find_element(By.NAME, button)

    def set_checkbox(self, checkbox):
        self.window.find_element(By.NAME, checkbox).click()

    def close(self):
        closeButton = self.window.find_element(By.ID, 'Close')
        closeButton.click()