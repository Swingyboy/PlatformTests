from windows.dialogWindow.baseDialogWindow import DialogWindow
from selenium.common.exceptions import WebDriverException as Error


class CopyUserSettingsWindow(DialogWindow):

    def __init__(self, driver):
        DialogWindow.__init__(self, driver, 'Copy user settings')


    def copy_setting(self, confirmation:bool):
        if confirmation:
            self.click_button('Yes')
        else:
            self.click_button('No')


class ExitWindow(DialogWindow):

    def __init__(self, driver):
        DialogWindow.__init__(self, driver, 'Exit')


    def shutdown(self):
        self.set_radiobutton_value('Shutdown')
        self.click_button('OK')


    def logoff(self):
        self.set_radiobutton_value('Logoff')
        self.click_button('OK')


class MessageWindow(DialogWindow):

    def __init__(self, driver):
        DialogWindow.__init__(self, driver, 'Message')

    def confirm(self):
        self.click_button('OK')


class WarningWindow(DialogWindow):

    def __init__(self, driver):
        DialogWindow.__init__(self, driver, 'Warning')


    def confirm(self):
        self.click_button('OK')