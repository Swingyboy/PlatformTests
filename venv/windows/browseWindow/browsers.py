from pynput.mouse import Button
from pynput.mouse import Controller as Mouse
from windows.browseWindow.baseBrowser import Browser

def mouse_move_down(mouse, value):
    x, y = mouse.position
    y += value
    mouse.position = (x, y)


class UserProfileBrowse(Browser):

    def __init__(self, driver):
        Browser.__init__(self, driver, 'User Profile Manager')


    def select_user(self, name):
        self.filter_items(name)
        mouse = Mouse()
        mouse_move_down(mouse, 40)
        mouse.click(Button.left)


class UserSiterRights(Browser):

    def __init__(self, driver, user, user_group):
        Browser.__init__(self, driver, 'Site rights for "' + user +'"'+ ' ['+user_group.upper()+']')