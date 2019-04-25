from selenium.webdriver.common.by import By


class LoginPage():

    def __init__(self, driver):
        self.driver = driver
        self.window = self.driver.find_element(By.NAME, 'API PRO login...')

    def get_user_value(self):
        return self.window.find_element(By.ID, '120').get_attribute('Name')

    def get_password_value(self):
        return self.window.find_element(By.ID, '122').get_attribute('Name')

    def get_language_value(self):
        return self.window.find_element(By.ID, '115').get_attribute('Name')

    def get_checkbox_value(self):
        return self.window.find_element(By.ID, '124').get_attribute("ToggleState")

    def get_user_label(self):
        return self.window.find_element(By.ID, '119').get_attribute('Name')

    def get_password_label(self):
        return self.window.find_element(By.ID, '121').get_attribute('Name')

    def get_language_label(self):
        return self.window.find_element(By.ID, '123').get_attribute('Name')

    def get_checkbox_lable(self):
        return self.window.find_element(By.ID, '124').get_attribute('Name')

    def set_user_value(self, value):
        self.window.find_element(By.ID, '120').send_keys(value)

    def set_password_value(self, value):
        self.window.find_element(By.ID, '122').send_keys(value)

    def set_checkbox_value(self):
        checkBox = self.window.find_element(By.ID, '124')
        checkBox.click()

    def click_cancel_buton(self):
        okButton = self.window.find_element_by_id("125")
        okButton.click()

    def click_ok_buton(self):
        okButton = self.window.find_element_by_id("114")
        okButton.click()

    def login(self, username, password):
        self.set_user_value(username)
        self.set_password_value(password)
        self.click_ok_buton()





