from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException as Error


class Apicbf():

    def __init__(self, driver, name):
        self.window = driver.find_element(By.NAME, name)


    def _find_item(self, win, item_id, id_type):
        if id_type == 'NAME':
            item = win.find_element(By.NAME, item_id)
        elif id_type == 'ID':
            item = win.find_element(By.ID, item_id)
        elif id_type == 'CLASS':
            item = win.find_element(By.CLASS_NAME, item_id)
        else:
            raise  Exception('Wrong search type!')
        return item


    def click_button(self, name):
        button = self._find_item(self.window, name, 'NAME')
        button.click()


    def get_title(self):
        return self.window.get_attribute('Name')


    def close(self):
        try:
            closeButton = self._find_item(self.window, 'Close', 'ID')
            closeButton.click()
        except Error:
            print('Unable to close this window! There is no CLOSE button!')


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