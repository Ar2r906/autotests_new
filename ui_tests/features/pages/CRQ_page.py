from typing import Literal

from ui_tests.features.pages.base_page import BasePage
from ui_tests.features.pages.locators.CRQ_locators import CrqPageLocators
from datetime import datetime, timedelta
from ui_tests.features.utills.logging.logger import get_logger

logger = get_logger()


class CrqPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.locators = CrqPageLocators(page)

    def choose_it_system(self, system):
        self.locators.it_system.click()
        self.locators.it_system.fill(system)

    def choose_change_type(self, option):
        self.locators.change_type.select_option(f'{option}')

    def choose_impact(self, option):
        self.locators.impact.select_option(f'{option}')

    def fill_date(self):
        start = datetime.now() + timedelta(hours=1)
        self.locators.date_start.fill(start.strftime("%d.%m.%Y %H:%M"))
        end = start + timedelta(hours=1)
        self.locators.date_end.fill(end.strftime("%d.%m.%Y %H:%M"))

    def choose_checkbox(self, text, option):
        self.locators.checkbox_option(text, option).click()

    def fill_description(self, description):
        self.locators.description_field.fill(description)

    def fill_testing_description(self, testing_description):
        self.locators.testing_description.fill(testing_description)

    def fill_return_plan(self, return_plan):
        self.locators.return_plan.fill(return_plan)

    def fill_change_description(self, change_description):
        self.locators.change_description.fill(change_description)

    def fill_form(self, role: Literal["Координатор", "Ответственный", "Исполнитель"],
                  first_arg: str, second_arg: str, third_arg: str):
        role_button = self.locators.choose_role_in_form(role)
        role_button.click()
        if role == "Координатор":
            buffer = "КЦ ЕХД Задачи и Изменения"
        else:
            buffer = "nnkornil10"
        self.locators.crq_search_field.fill(buffer)
        self.page.get_by_role("link", name=first_arg).click()
        self.page.get_by_role("link", name=second_arg).click()
        self.page.get_by_role("button", name=third_arg).click()
