from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException as Error

class Browser():

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


    def _get_filter(self):
        return self._find_item(self.window, 'QuickFilter', 'NAME')


    def click_button(self, name):
        button = self._find_item(self.window, name, 'NAME')
        button.click()


    def get_title(self):
        return self.window.get_attribute('Name')


    def filter_ok(self):
        button = _find_item(self._get_filter, 'OK', 'NAME')
        button.click()


    def filter_clear(self):
        button = _find_item(self._get_filter, 'Clear', 'NAME')
        button.click()


    def filter_load(self):
        button = _find_item(self._get_filter, 'Load', 'NAME')
        button.click()


    def filter_items(self, field, value, operator):
        qfil = self._get_filter()
        filterOn = self._find_item(qfil, 'Field to filter on', 'NAME')
        filterOn.click()


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

