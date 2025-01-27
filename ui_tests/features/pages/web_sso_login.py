from ui_tests.features.pages.base_page import BasePage
from ui_tests.features.pages.locators.web_sso_locators import *


class WebSSOLoginPage(BasePage):

    def login_user(self, user_name, password):
        self.page.wait_for_selector('iframe')
        iframe_element = self.page.query_selector('iframe')
        iframe = iframe_element.content_frame()

        # Дожидаемся элемента по ID внутри iframe
        login_edit = iframe.wait_for_selector(USER_INPUT)
        password_edit = iframe.wait_for_selector(PASS_INPUT)
        login_button = iframe.wait_for_selector(SUBMIT_BUTTON)

        login_edit.fill(user_name)
        password_edit.fill(password)
        login_button.click()
