from playwright.sync_api import Locator
from ui_tests.features.utills.logging.logger import get_logger

from ui_tests.features.pages.locators.base_locators import BasePageLocators

logger = get_logger()


class TasPageLocators(BasePageLocators):
    def __init__(self, page):
        super().__init__(page)
        self.operator_info_field = self.page.get_by_test_id("custom_select_assign_users_input")

    def find_console_row(self, text) -> Locator:
        """
        :param text: Название поля в консоли.
        :return: Элемент.
        Пример отдельного локатора : self.tas_type = self.page.get_by_text("Тип задачи").
        """
        return self.page.get_by_text(text)

    def find_checkbox_by_row_name(self, rowname) -> Locator:
        """
        :param rowname: Название поля в консоли, меню которого необходимо открыть.
        :return: Элемент.
        """
        if rowname == 'Статус':
            row = self.page.locator("#console-select-1")
        elif rowname == 'Причина состояния':
            row = self.page.locator("#console-select-2")
        elif rowname == 'Назначенная группа':
            row = self.page.locator("#console-select-3")
        else:
            row = None
            logger.info('Поле не найдено')
        return row
