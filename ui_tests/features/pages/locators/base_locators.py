import typing

from playwright.sync_api import Locator

from ui_tests.features.pages.base_page import BasePage


class BasePageLocators(BasePage):
    def __init__(self, page):
        super().__init__(page)
        # self.chat_button = self.page.query_selector('div.button-open')
        self.text_area = self.page.get_by_role("textbox", name="Поле ввода")
        self.console_tas = self.page.get_by_role("link", name="Задачи")
        self.console_inc = self.page.get_by_role("link", name="Инциденты")
        self.registration_crq = self.page.get_by_role("heading", name="Регистрация изменения")
        self.search_field = self.page.get_by_test_id("console-search-input")
        self.logout = self.page.get_by_role("button", name="Sign in")
        self.statuses = self.page.get_by_role("button", name="Статусы")
        self.status_all = self.page.get_by_role("menuitem", name="Все")
        self.status_open = self.page.get_by_role("menuitem", name="Открытые")
        self.status_closed = self.page.get_by_role("menuitem", name="Закрытые")

    def get_user_name(self) -> Locator | str:
        """Возвращает имя залогиненного пользователя"""
        return self.page.get_by_test_id('profile_name')

    def get_operator_name(self) -> Locator | str:
        """Возвращает 'Назначенное лицо' из открытой карточки"""
        return self.page.locator(".toggle-block__content-row-block")

    def get_card_status(self, status):
        return self.page.get_by_text(f"Статус: {status}", exact=False)

    def get_elements_count(self):
        return self.page.wait_for_selector(
            '.tableFooter label[class*="mr-5"]', timeout=1000
        ).inner_text().split()[-1]
