from pynput.mouse import Button
from pynput.mouse import Controller as Mouse
from windows.apicbfWindow.baseApicbf import Apicbf


class UserPermissionsWindow(Apicbf):

    def __init__(self, driver):
        Apicbf.__init__(self, driver, 'User Permissions')

    def get_full_permission(self):
        self.click_button('All programs')
        self.click_button('All')
        self.click_button('Grant now')


class PropertiesWindow(Apicbf):

    def __init__(self, driver):
        Apicbf.__init__(self, driver, 'Properties explorer')
        self.tree_items = {'Basic module':'                        ',
                           'Default account configuration':'                                                       ',
                           'Document configuration':'                                             ',
                           'Stock configuration':'                                    ',
                           'Purchase configuration':'                                           ',
                           'Maintenance configuration':'                                                  ',
                           'Inspection configuration':'                                              ',
                           'Bar code configuration':'                                          ',
                           'Handterminal configuration':'                                                   ',
                           'Mobile':'            ',
                           'Calibration configuration':'                                              ',
                           'Service module configuration':'                                                       ',
                           'Transactions locking':'                                      '}


    def get_tree(self):
        propetiesTree = self._find_item(self.window, 'SysTreeView32', 'CLASS')
        return propetiesTree


    def open_tree_item(self, field):
        tree = self.get_tree()
        item = tree.find_element_by_name(self.tree_items[field])
        item.click()
        mouse = Mouse()
        mouse.click(Button.left, 2)
