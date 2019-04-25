from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException as Error


class DialogWindow():

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

    def click_button(self, button):
        button = self._find_item(self.window, button, 'NAME')
        button.click()

    def get_checkbox_value(self, id, search = 'NAME'):
        chbox = self._find_item(self.window, id, search)
        return chbox, chbox.is_selected()

    def set_checkbox_value(self, id, value:bool, search = 'NAME'):
        chbox, chboxValue = self.get_checkbox_value(id, search)
        if chboxValue == value:
            pass
        else:
            chbox.click()

    def set_radiobutton_value(self, id, search = 'NAME'):
        button, value = self.get_checkbox_value(id, search)
        if value == True:
            pass
        else:
            button.click()

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