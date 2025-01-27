import typing

from playwright.sync_api import Locator

from ui_tests.features.pages.base_page import BasePage


class CrqPageLocators(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.it_system = self.page.get_by_role("textbox", name="Выберите")
        self.change_type = self.page.get_by_role("group", name="Тип изменения (класс)").locator("select")
        self.impact = self.page.get_by_role("group", name="Влияние").locator("select")
        self.description_field = self.page.get_by_role("textbox", name="Введите")
        self.date_start = self.page.get_by_role("group", name="Плановое начало").get_by_role("textbox")
        self.date_end = self.page.get_by_role("group", name="Плановое окончание").get_by_role("textbox")
        self.testing_description = self.page.get_by_role(
            "group", name="Информация о тестировании").get_by_placeholder("Причины отсутствия тестирования")
        self.return_plan = self.page.get_by_role(
            "group", name="План возврата").get_by_placeholder("Введите текст")
        self.change_description = self.page.get_by_role(
            "group", name="Основание для изменения").get_by_placeholder("Введите текст")
        self.save_draft = self.page.get_by_role("group", name="Сохранить черновик").get_by_role("button")
        self.crq_search_field = self.page.get_by_placeholder("Начните вводить группу или ФИО или логин")
        self.crq_reg_modal = self.page.locator('.modal-content')
        self.crq_modal_number = self.page.get_by_text("CRQ")

    def choose_role_in_form(self, role: str) -> Locator:
        return self.page.get_by_role("group", name=role).get_by_role("button")

    def checkbox_option(self, text: str, option: str) -> Locator:
        return self.page.get_by_role('group').filter(has_text=text).get_by_text(option)
