import pytest
import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from windows import LoginWindow, MainWindow
from windows.dialogWindow.dialogWindows import WarningWindow, ExitWindow, CopyUserSettingsWindow
from windows.browseWindow import UserProfileBrowse
from windows.maintWindow.maints import UserMaint
from windows.selectWindow.ResetPasswordWindow import ResetPassworWindow


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

        userLabel = loginPage.get_user_label()
        assert userLabel == 'User ID:'

        passwordLabel = loginPage.get_password_label()
        assert passwordLabel == 'Password:'

        languageLabel = loginPage.get_language_label()
        assert languageLabel == 'Language:'

        languageDropDown = loginPage.get_language_value()
        assert languageDropDown

        checkBoxLabel = loginPage.get_checkbox_lable()
        assert checkBoxLabel == 'Remember me'

        if loginPage.get_checkbox_value() == 'Off':
            loginPage.set_checkbox_value()

        loginPage.login(self.user, self.password)
        time.sleep(2)
        try:
            warningPage = WarningWindow(loginPage.window)
        except WebDriverException:
            warningPage = None

        if warningPage:
            warningPage.confirm()

        time.sleep(2)

        mainWindow = MainWindow.MainWindow(self.driver)
        mainWindow.close()

        time.sleep(2)
        try:
            exitPage = ExitWindow(self.driver)
        except WebDriverException:
            exitPage = None

        if exitPage:
            exitPage.shutdown()

        time.sleep(2)
        driver = webdriver.Remote(command_executor='http://localhost:9999',
                                  desired_capabilities={'debugConnectToRunningApp': 'false',
                                                        'app': self.appPath})
        time.sleep(2)

        loginPage = LoginWindow.LoginPage(driver)

        userID = loginPage.get_user_value()
        assert userID.lower() == self.user.lower()

        passwrd = loginPage.get_password_value()
        assert  passwrd == self.password

        language = loginPage.get_language_value()
        assert language == 'English'

        loginPage.click_cancel_buton()


    def test_login_as_supervisor(self, startUp):
        loginPage = LoginWindow.LoginPage(self.driver)
        loginPage.login('supervisor', '')
        time.sleep(2)
        try:
            warningPage = WarningWindow(loginPage.window)
        except WebDriverException:
            warningPage = None

        if warningPage:
            warningPage.confirm()
        time.sleep(2)

        mainWindow = MainWindow.MainWindow(self.driver)

        assert mainWindow.get_title() == 'API PRO 9 - 9.0SP00C - QA [SUPERVISOR]'

        mainWindow.close()

        time.sleep(2)
        try:
            exitPage = ExitWindow(self.driver)
        except WebDriverException:
            exitPage = None

        if exitPage:
            exitPage.shutdown()


    def test_create_test_user(self, startUp):
        loginPage = LoginWindow.LoginPage(self.driver)
        loginPage.login('supervisor', '')
        time.sleep(2)
        try:
            warningPage = WarningWindow(loginPage.window)
        except WebDriverException:
            warningPage = None

        if warningPage:
            warningPage.confirm()
        time.sleep(2)

        mainWindow = MainWindow.MainWindow(self.driver)
        time.sleep(2)

        systemItem = mainWindow.get_menu_item('Menu Bar', 'System')
        userMenu = mainWindow.get_menu_item('System', 'User')
        userProfileItem = mainWindow.get_menu_item('User', 'User profile manager')
        userProfileItem.click()
        time.sleep(12)

        userProfileWindow = UserProfileBrowse.UserProfileBrowse(self.driver)
        newButton = userProfileWindow.get_menu_item('Toolbar', 'New')
        newButton.click()
        time.sleep(5)

        userMaintWindow = UserMaint(userProfileWindow.window)
        userMaintWindow.create_supervisor_user('SBE9')
        saveButton = userProfileWindow.get_menu_item('Toolbar', 'Save')
        saveButton.click()
        time.sleep(2)

        dialogWindow = CopyUserSettingsWindow(userMaintWindow.window)
        dialogWindow.copy_setting(False)
        time.sleep(2)

        passwordWindow = ResetPassworWindow(userMaintWindow.window)
        assert passwordWindow

'''    def test_assign_password_to_the_test_user(self):
        passwordWindow = ResetPassworWindow(userMaintWindow.window)
        passwordWindow.set_checkbox('Prompt user for new password at next login')
        okButton = passwordWindow.get_button('OK')
        okButton.click()
'''









