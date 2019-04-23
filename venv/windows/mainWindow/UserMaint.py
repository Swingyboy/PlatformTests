from selenium.webdriver.common.by import By

class UserMaint():

    def __init__(self, driver):
        self.window = driver.find_element(By.NAME, 'User')

    def getTitle(self):
        return self.window.get_attribute('Name')

    def getMenuItem(self, menu, item):
        menuBar = self.window.find_element(By.NAME, menu)
        menuBar.click()
        return menuBar.find_element(By.NAME, item)

    def setField(self, field, value):
        field = self.window.find_element(By.NAME, field)
        id = int(field.get_attribute('AutomationId'))
        id -=1
        field = self.window.find_element(By.ID, id)
        field.send_keys(value)

    def setDropDown(self, field, value):
        field = self.window.find_element(By.NAME, field)
        id = int(field.get_attribute('AutomationId'))
        id -=1
        field = self.window.find_element(By.ID, id)
        field.click()
        if isinstance(value, str):
            item = field.find_element(By.NAME, value)
        if isinstance(value, int):
            item = field.find_element(By.ID, value)
        item.click()

    def close(self):
        closeButton = self.window.find_element(By.ID, 'Close')
        closeButton.click()