import pytest
import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from windows import LoginWindow, MainWindow
from windows.dialogWindow.dialogWindows import WarningWindow, ExitWindow, MessageWindow, CopyUserSettingsWindow
from windows.browseWindow import UserProfileBrowse
from windows.maintWindow.maints import UserMaint
from windows.selectWindow.ResetPasswordWindow import ResetPassworWindow


@pytest.fixture()
def startUp():
    global DRIVER
    global APPLICATION_PATH
    APPLICATION_PATH = r'C:\APIPRO9\reference-90sp00c_qa\client.cmd'
    DRIVER = webdriver.Remote(command_executor='http://localhost:9999',
                              desired_capabilities={'debugConnectToRunningApp': 'false','app': APPLICATION_PATH})
    user = 'supervisor'
    password = ''
    time.sleep(2)
    return DRIVER, user, password


def test_start_apipro(startUp):
    driver, user, password = startUp
    loginPage = LoginWindow.LoginPage(driver)

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
    loginPage.login(user, password)
    time.sleep(2)

    try:
        warningPage = WarningWindow(loginPage.window)
    except WebDriverException:
        warningPage = None

    if warningPage:
        warningPage.confirm()
    time.sleep(2)

    mainWindow = MainWindow.MainWindow(driver)
    mainWindow.close()
    time.sleep(2)

    try:
        exitPage = ExitWindow(driver)
    except WebDriverException:
        exitPage = None

    if exitPage:
        exitPage.shutdown()
    time.sleep(2)

    driver = webdriver.Remote(command_executor='http://localhost:9999',
                              desired_capabilities={'debugConnectToRunningApp': 'false','app': APPLICATION_PATH})
    time.sleep(2)

    loginPage = LoginWindow.LoginPage(driver)
    userID = loginPage.get_user_value()
    assert userID.lower() == user.lower()

    pswd = loginPage.get_password_value()
    assert  pswd == password

    language = loginPage.get_language_value()
    assert language == 'English'
    loginPage.click_cancel_buton()


def test_login_as_supervisor(startUp):
    driver, user, password = startUp
    loginPage = LoginWindow.LoginPage(driver)
    loginPage.login(user, password)
    time.sleep(2)
    try:
        warningPage = WarningWindow(loginPage.window)
    except WebDriverException:
        warningPage = None

    if warningPage:
        warningPage.confirm()
    time.sleep(2)

    mainWindow = MainWindow.MainWindow(driver)
    assert mainWindow.get_title() == 'API PRO 9 - 9.0SP00C - QA [SUPERVISOR]'


def test_create_test_user():
    mainWindow = MainWindow.MainWindow(DRIVER)
    time.sleep(2)

    systemItem = mainWindow.get_menu_item('Menu Bar', 'System')
    userMenu = mainWindow.get_menu_item('System', 'User')
    userProfileItem = mainWindow.get_menu_item('User', 'User profile manager')
    userProfileItem.click()
    time.sleep(12)

    userProfileWindow = UserProfileBrowse.UserProfileBrowse(DRIVER)
    userProfileWindow.click_button('New')
    time.sleep(5)

    userMaintWindow = UserMaint(userProfileWindow.window)
    userMaintWindow.create_supervisor_user('SBE9')
    userMaintWindow.click_button('Save')
    time.sleep(2)

    dialogWindow = CopyUserSettingsWindow(userMaintWindow.window)
    dialogWindow.copy_setting(False)
    time.sleep(2)

    passwordWindow = ResetPassworWindow(userMaintWindow.window)
    assert passwordWindow


def test_assign_password_to_the_test_user():
    passwordWindow = ResetPassworWindow(DRIVER)
    passwordWindow.set_checkbox('Prompt user for new password at next login')
    okButton = passwordWindow.get_button('OK')
    okButton.click()
    messageWind = MessageWindow(DRIVER)
    assert messageWind
    messageWind.confirm()


def test_set_approval_rights_to_the_test_user():
    userMaintWindow = UserMaint(DRIVER)
    assert not userMaintWindow.element_is_enable('Save')
    userMaintWindow.set_full_approval_rights('SBE9')
    assert userMaintWindow.element_is_enable('Save')
    userMaintWindow.click_button('Save')
    time.sleep(5)

    assert not userMaintWindow.element_is_enable('Save')
    assert userMaintWindow.get_value('API user:') == 'SBE9'
    userMaintWindow.close()











