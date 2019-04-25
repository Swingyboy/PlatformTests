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
                    field_values:dict={},
                    checkbox_value:dict={}
                    ):

        self.set_field_value('API user:', user)
        self.set_field_value('User group:', userGroup)
        self.set_dropdown_value('License:', lic)

        for tab in self.tabs:
            if 'WO max amount:' in field_values[tab]:
                try:
                    self._set_wo_max_amount(field_values[tab]['WO max amount:'])
                    field_values[tab].pop('WO max amount:')
                except Error:
                    pass
            if 'Ignore restrict.' in checkbox_value[tab]:
                try:
                    self._set_ignore_rest(checkbox_value[tab]['Ignore restrict.'])
                    checkbox_value[tab].pop('Ignore restrict.')
                except Error:
                    pass
            for field, value in list(field_values[tab].items()):
                try:
                    self.set_field_value(field, value)
                    field_values[tab].pop(field)
                except Error:
                    pass
            for ch, value in list(checkbox_value[tab].items()):
                try:
                    self.set_checkbox_value(ch, value)
                    checkbox_value[tab].pop(ch)
                except Error:
                    pass
            self.switch_tab()


    def create_supervisor_user(self, name):
        fields = {'Main':
                      {'Name:': 'Test supervisor user',
                  'Contact person:': 'Festo sales'},
                  'Approval':
                      {'Req. header max:': 999999,
                  'Request max:': 999999,
                  'PO max amount:': 999999,
                  'Agreement max:' :999999,
                  'Invoice max:': 999999,
                  'Inv. app. tol.:': 999999,
                  'Inv. app. tol. %:': 999,
                  'WO max amount:': 999999},
                  'Extra setup':
                      {'Recent values:': 5},
                  'PDA setup':{},
                  'Extra info':{}
                  }

        checkboxes = {'Main':
                          {'Change key in trans.': True,
                           'Supervisor': True,
                           'Shift resp.': True,
                           'Purchaser': True,
                           'Technical responsible': True},
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

        self.create_user(name,'System','Full named license',fields,checkboxes)

