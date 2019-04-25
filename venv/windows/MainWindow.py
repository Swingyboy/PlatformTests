from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException as Error


class MainWindow():

    def __init__(self, driver):
        self.window = driver.find_element(By.CLASS_NAME, 'ProMainWin')

    def get_title(self):
        return self.window.get_attribute('Name')

    def get_menu_item(self, menu, item):
        menuBar = self.window.find_element(By.NAME, menu)
        menuBar.click()
        return menuBar.find_element(By.NAME, item)

    def close(self):
        try:
            closeButton = self._find_item(self.window, 'Close', 'ID')
            closeButton.click()
        except Error:
            print('Unable to close this window! There is no CLOSE button!')

    def restore(self):
        try:
            maxButton = self._find_item(self.window, 'Restore', 'ID')
            maxButton.click()
        except Error:
            print('Unable to restore this window! There is no RESTORE button!')

    def maximize(self):
        try:
            maxButton = self._find_item(self.window, 'Maximize', 'ID')
            maxButton.click()
        except Error:
            print('Unable to maximize this window! There is no MAXIMIZE button!')

    def minimize(self):
        try:
            minButton = self.w_find_item(self.window, 'Minimize', 'ID')
            minButton.click()
        except Error:
            print('Unable to minimize this window! There is no MINIMIZE button!')