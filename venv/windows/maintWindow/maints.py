from windows.maintWindow.baseMaint import Maint
from selenium.common.exceptions import WebDriverException as Error

class UserMaint(Maint):

    def __init__(self, driver):
        Maint.__init__(self, driver, 'User')
        self.tabs = ['Main', 'Approval', 'Extra setup', 'PDA setup', 'Extra info']


    def _set_ignore_rest(self, value):
        chboxes = self.window.find_elements_by_name('Ignore restrict.')
        for ch in chboxes:
           if ch.is_selected() == value:
               pass
           else:
               ch.click()


    def _set_wo_max_amount(self, value):
        chboxes = self.window.find_elements_by_name('Ignore restrict.')
        for ch in chboxes:
            id = int(ch.get_attribute('AutomationId')) + 1
            field = self.window.find_element_by_id(id)
            field.send_keys(value)


    def create_user(self, user:str,
                    userGroup:str = 'System',
                    lic='Technical named license',
                    field_value:dict={},
                    checkbox_value:dict={}
                    ):
        self.set_field_value('API user:', user)
        self.set_field_value('User group:', userGroup)
        self.set_dropdown_value('License:', lic)
        self.set_rights(user, field_value, checkbox_value)


    def create_supervisor_user(self, name):
        fields = {'Main':
                      {'Name:': 'Test supervisor user',
                       'Contact person:': 'Festo sales'},
                  'Approval':{},
                  'Extra setup':
                      {'Recent values:': 5},
                  'PDA setup': {},
                  'Extra info': {}
                  }
        checkboxes = {'Main':
                          {'Change key in trans.': True,
                           'Supervisor': True,
                           'Shift resp.': True,
                           'Purchaser': True,
                           'Technical responsible': True},
                      'Approval':{},
                      'Extra setup':
                          {'Allow viewing hour registrations for other work suppliers': True},
                      'PDA setup': {},
                      'Extra info': {}
                      }
        self.create_user(name, lic='Full named license', field_value=fields, checkbox_value=checkboxes)


    def set_rights(self, name, fields: dict = {}, checkboxes: dict = {}):

        field_values = {'Main':{},
                  'Approval':{},
                  'Extra setup':{},
                  'PDA setup': {},
                  'Extra info': {}
                  }

        checkbox_values = {'Main':{},
                      'Approval':{},
                      'Extra setup':{},
                      'PDA setup': {},
                      'Extra info': {}
                      }

        for (key1, key2) in zip(field_values.keys(), fields):
            field_values[key1].update(fields[key2])
        for (key1, key2) in zip(checkbox_values.keys(), checkboxes.keys()):
            checkbox_values[key1].update(checkboxes[key2])

        while True:
            try:
                self._find_item(self.window, 'Plant key:', 'NAME' )
                break
            except Error:
                self.switch_tab()

        self.set_field_value('API user:', name)
        self.click_tab()

        for tab in self.tabs:
            if 'WO max amount:' in field_values[tab]:
                try:
                    self._set_wo_max_amount(field_values[tab]['WO max amount:'])
                    field_values[tab].pop('WO max amount:')
                except Error:
                    pass
            if 'Ignore restrict.' in checkbox_values[tab]:
                try:
                    self._set_ignore_rest(checkbox_values[tab]['Ignore restrict.'])
                    checkbox_values[tab].pop('Ignore restrict.')
                except Error:
                    pass
            for field, value in list(field_values[tab].items()):
                try:
                    self.set_field_value(field, value)
                    field_values[tab].pop(field)
                except Error:
                    pass
            for ch, value in list(checkbox_values[tab].items()):
                try:
                    self.set_checkbox_value(ch, value)
                    checkbox_values[tab].pop(ch)
                except Error:
                    pass
            self.switch_tab()


    def set_full_approval_rights(self, name):
        field_values = {'Main':{},
                  'Approval':
                      {'Req. header max:': 999999,
                       'Request max:': 999999,
                       'PO max amount:': 999999,
                       'Agreement max:': 999999,
                       'Invoice max:': 999999,
                       'Inv. app. tol.:': 999999,
                       'Inv. app. tol. %:': 999,
                       'WO max amount:': 999999},
                  'Extra setup':{},
                  'PDA setup': {},
                  'Extra info': {}
                  }
        checkbox_values = {'Main':{},
                      'Approval':
                          {'Overrule appr.': True,
                           'Approve service invoice': True,
                           'Enable motify': True,
                           'Edit CAL WO': True,
                           'Approve request header': True,
                           'Approve request': True,
                           'Approve PO': True,
                           'Ignore restrict.': True,
                           'Approve invoice': True,
                           'Approve WO': True,
                           'Tech. approve WO': True,
                           'Approve WO finish': True,
                           'Ignore restrict.': True,
                           'Approve MO 1': True,
                           'Approve MO 2': True,
                           'Approve MO 3': True,
                           'Approval 1': True,
                           'Approval 2': True,
                           'Approve permit': True,
                           'Approve permit 2': True,
                           'Approve permit template': True},
                      'Extra setup':
                          {'Allow viewing hour registrations for other work suppliers': True},
                      'PDA setup': {},
                      'Extra info': {}
                      }
        self.set_rights(name, field_values, checkbox_values)






