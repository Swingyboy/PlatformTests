from selenium.webdriver.common.by import By

class MainWindow():

    def __init__(self, driver):
        self.window = driver.find_element(By.CLASS_NAME, 'ProMainWin')

    def getTitle(self):
        return self.window.get_attribute('Name')

    def getMenuItem(self, menu, item):
        menuBar = self.window.find_element(By.NAME, menu)
        menuBar.click()
        return menuBar.find_element(By.NAME, item)

    def close(self):
        closeButton = self.window.find_element(By.ID, 'Close')
        closeButton.click()