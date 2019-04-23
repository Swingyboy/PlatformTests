from selenium.webdriver.common.by import By


class LoginPage():

    def __init__(self, driver):
        self.driver = driver
        self.window = self.driver.find_element(By.NAME, 'API PRO login...')

    def getUserValue(self):
        return self.window.find_element(By.ID, '120').get_attribute('Name')

    def getPasswordValue(self):
        return self.window.find_element(By.ID, '122').get_attribute('Name')

    def getLanguageValue(self):
        return self.window.find_element(By.ID, '115').get_attribute('Name')

    def getCheckBoxValue(self):
        return self.window.find_element(By.ID, '124').get_attribute("ToggleState")

    def getUserLabel(self):
        return self.window.find_element(By.ID, '119').get_attribute('Name')

    def getPasswordLabel(self):
        return self.window.find_element(By.ID, '121').get_attribute('Name')

    def getLanguageLabel(self):
        return self.window.find_element(By.ID, '123').get_attribute('Name')

    def getCheckBoxLable(self):
        return self.window.find_element(By.ID, '124').get_attribute('Name')

    def setUserValue(self, value):
        self.window.find_element(By.ID, '120').send_keys(value)

    def setPasswordValue(self, value):
        self.window.find_element(By.ID, '122').send_keys(value)

    def setCheckBoxValue(self):
        checkBox = self.window.find_element(By.ID, '124')
        checkBox.click()

    def clickCancelButon(self):
        okButton = self.window.find_element_by_id("125")
        okButton.click()

    def clickOKButon(self):
        okButton = self.window.find_element_by_id("114")
        okButton.click()

    def login(self, username, password):
        self.setUserValue(username)
        self.setPasswordValue(password)
        self.clickOKButon()





