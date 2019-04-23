import pytest
import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from windows import LoginWindow, MainWindow
from windows.dialogWindow import WarningWindow, ExitWindow, CopyUserSettingsWindow
from windows.browseWindow import UserProfileBrowse
from windows.mainWindow import UserMaint, ResetPasswordWindow


class TestFirstRun():

    @pytest.fixture()
    def startUp(self):
        self.appPath = r'C:\APIPRO9\reference-90sp00c_qa\client.cmd'
        self.driver = webdriver.Remote(command_executor='http://localhost:9999',
                                  desired_capabilities={'debugConnectToRunningApp': 'false',
                                  'app':self.appPath})
        self.user = 'supervisor'
        self.password = ''
        time.sleep(2)


    def test_start_apipro(self, startUp):
        loginPage = LoginWindow.LoginPage(self.driver)

        userLabel = loginPage.getUserLabel()
        assert userLabel == 'User ID:'

        passwordLabel = loginPage.getPasswordLabel()
        assert passwordLabel == 'Password:'

        languageLabel = loginPage.getLanguageLabel()
        assert languageLabel == 'Language:'

        languageDropDown = loginPage.getLanguageValue()
        assert languageDropDown

        checkBoxLabel = loginPage.getCheckBoxLable()
        assert checkBoxLabel == 'Remember me'

        if loginPage.getCheckBoxValue() == 'Off':
            loginPage.setCheckBoxValue()

        loginPage.login(self.user, self.password)
        time.sleep(2)
        try:
            warningPage = WarningWindow.WarningPage(loginPage.window)
        except WebDriverException:
            warningPage = None

        if warningPage:
            warningPage.close()

        time.sleep(2)

        mainWindow = MainWindow.MainWindow(self.driver)
        mainWindow.close()

        time.sleep(2)
        try:
            exitPage = ExitWindow.ExitPage(self.driver)
        except WebDriverException:
            exitPage = None

        if exitPage:
            exitPage.close()

        time.sleep(2)
        driver = webdriver.Remote(command_executor='http://localhost:9999',
                                  desired_capabilities={'debugConnectToRunningApp': 'false',
                                                        'app': self.appPath})
        time.sleep(2)

        loginPage = LoginWindow.LoginPage(driver)

        userID = loginPage.getUserValue()
        assert userID.lower() == self.user.lower()

        passwrd = loginPage.getPasswordValue()
        assert  passwrd == self.password

        language = loginPage.getLanguageValue()
        assert language == 'English'

        loginPage.clickCancelButon()


    def test_login_as_supervisor(self, startUp):
        loginPage = LoginWindow.LoginPage(self.driver)
        loginPage.login('supervisor', '')
        time.sleep(2)
        try:
            warningPage = WarningWindow.WarningPage(loginPage.window)
        except WebDriverException:
            warningPage = None

        if warningPage:
            warningPage.close()
        time.sleep(2)

        mainWindow = MainWindow.MainWindow(self.driver)

        assert mainWindow.getTitle() == 'API PRO 9 - 9.0SP00C - QA [SUPERVISOR]'

        mainWindow.close()

        time.sleep(2)
        try:
            exitPage = ExitWindow.ExitPage(self.driver)
        except WebDriverException:
            exitPage = None

        if exitPage:
            exitPage.close()


    def test_create_test_user(self, startUp):
        loginPage = LoginWindow.LoginPage(self.driver)
        loginPage.login('supervisor', '')
        time.sleep(2)
        try:
            warningPage = WarningWindow.WarningPage(loginPage.window)
        except WebDriverException:
            warningPage = None

        if warningPage:
            warningPage.close()
        time.sleep(2)

        mainWindow = MainWindow.MainWindow(self.driver)
        time.sleep(2)

        systemItem = mainWindow.getMenuItem('Menu Bar', 'System')
        userMenu = mainWindow.getMenuItem('System', 'User')
        userProfileItem = mainWindow.getMenuItem('User', 'User profile manager')
        userProfileItem.click()
        time.sleep(5)

        userProfileWindow = UserProfileBrowse.UserProfileBrowse(self.driver)
        newButton = userProfileWindow.getMenuItem('Toolbar', 'New')
        newButton.click()
        time.sleep(5)

        userMaintWindow = UserMaint.UserMaint(userProfileWindow.window)
        userMaintWindow.setField('API user:', 'SBE9')
        userMaintWindow.setField('User group:', 'SYSTEM')
        userMaintWindow.setDropDown('License:', 'Full named license')
        saveButton = userProfileWindow.getMenuItem('Toolbar', 'Save')
        saveButton.click()
        time.sleep(2)

        dialogWindow = CopyUserSettingsWindow.CopyUserSettingsWindow(userMaintWindow.window)
        noButton = dialogWindow.getButton('No')
        noButton.click()
        time.sleep(2)

        passwordWindow = ResetPasswordWindow.ResetPassworWindow(userMaintWindow.window)
        passwordWindow.setCheckbox('Prompt user for new password at next login')
        okButton = passwordWindow.getButton('OK')
        okButton.click()




