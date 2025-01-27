from ui_tests.features.pages.base_page import BasePage
# from ui_tests.features.pages.locators.smart_tas_locators import CONSOLE_TAS
from ui_tests.features.pages.locators.web_sso_locators import *


class SmartMainPage(BasePage):

    def login_user(self, user_name, password):
        login_edit = self.wait_element(USER_INPUT)
        password_edit = self.wait_element(PASS_INPUT)
        login_button = self.wait_element(SUBMIT_BUTTON)

        login_edit.fill(user_name)
        password_edit.fill(password)
        login_button.click()

    def active_console(self, locator):
        console_name = self.wait_element(locator)
        console_name = console_name.text_content()
        print(console_name)
