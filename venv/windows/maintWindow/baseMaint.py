from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException as Error
from pynput.keyboard import Key, Controller

class Maint():

    def __init__(self, driver, name):
        self.window = driver.find_element(By.NAME, name)
        self.tabs = []

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

    def click_pns_button(self, name):
        field = self._find_item(self.window, name, 'NAME')
        id = int(field.get_attribute('AutomationId')) + 1
        button = self._find_item(self.window, id, 'ID')
        button.click()

    def click_tree_button(self, name):
        field = self._find_item(self.window, name, 'NAME')
        id = int(field.get_attribute('AutomationId')) + 2
        button = self._find_item(self.window, id, 'ID')
        button.click()

    def click_button(self, name):
        button = self._find_item(self.window, name, 'NAME')
        button.click()

    def get_checkbox_value(self, id, search = 'NAME'):
        chbox = self._find_item(self.window, id, search)
        return chbox, chbox.is_selected()

    def get_menu_item(self, menu, item):
        menuBar = self.window.find_element(By.NAME, menu)
        menuBar.click()
        return menuBar.find_element(By.NAME, item)

    def get_title(self):
        return self.window.get_attribute('Name')

    def get_value(self, field, search = 'NAME'):
        field = self._find_item(self.window, field, search)
        id = int(field.get_attribute('AutomationId')) - 1
        field = self._find_item(self.window, id, 'ID')
        return field.get_attribute('Name')

    def set_checkbox_value(self, id, value:bool, search = 'NAME'):
        chbox, chboxValue = self.get_checkbox_value(id, search)
        if chboxValue == value:
            pass
        else:
            chbox.click()

    def set_dropdown_value(self, field, value, search = 'NAME'):
        field = self._find_item(self.window, field, search)
        id = int(field.get_attribute('AutomationId')) - 1
        field = self._find_item(self.window, id, 'ID')
        field.click()
        item = self._find_item(field, value, 'NAME')
        item.click()

    def set_field_value(self, field, value, search = 'NAME'):
        field = self._find_item(self.window, field, search)
        id = int(field.get_attribute('AutomationId')) - 1
        field = self._find_item(self.window, id, 'ID')
        field.send_keys(value)

    def switch_tab(self):
        self.window.click()
        keyboard = Controller()
        keyboard.press(Key.ctrl)
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        keyboard.release(Key.ctrl)

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