import time

from ui_tests.features.pages.base_page import BasePage
from ui_tests.features.pages.locators.TAS_locators import TasPageLocators


class TasPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.locators = TasPageLocators(page)

    def fill_operator_field(self, data):
        self.locators.operator_info_field.fill(data)
