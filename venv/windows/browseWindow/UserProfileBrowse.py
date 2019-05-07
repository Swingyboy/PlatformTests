from windows.browseWindow.baseBrowser import Browser

class UserProfileBrowse(Browser):
    def __init__(self, driver):
        Browser.__init__(self, driver, 'User Profile Manager')
