import logging
import time
import typing
from typing import Literal

from playwright._impl._sync_base import mapping
from playwright.sync_api import Page, ElementHandle

from base.settings import settings


class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.base_url = settings.UI_SMART_BASE_URL

    def get_current_url(self) -> str:
        return self.page.url

    def check_current_url_is(self, expected_url: str):
        assert expected_url in self.page.url, 'Открылась другая страница'

    def wait_element(self, locator: str, timeout: int = 30) -> ElementHandle:
        return self.page.wait_for_selector(locator, timeout=timeout * 1000)

    def wait_page_loaded(self, state: Literal["domcontentloaded", "load", "networkidle"] = 'load', timeout: int = 40):
        self.page.wait_for_load_state(state, timeout=timeout * 1000)

    def check_is_disabled(self, locator: str, timeout: int = 20):
        assert self.wait_element(locator, timeout).is_disabled()

    def check_is_enabled(self, locator: str, timeout: int = 20):
        assert self.wait_element(locator, timeout).is_enabled()

    def check_is_editable(self, locator: str, timeout: int = 20):
        assert self.wait_element(locator, timeout).is_editable()

    def _and(self):
        return self

    def find_by_text(self, text: str, exact: bool = True):
        return self.page.get_by_text(text, exact=exact)

    def find_by_role(self, role, name=None, exact=None):
        return self.page.get_by_role(role, name=name, exact=exact)

    def fill_search_field(self, data: str):
        locator = self.page.get_by_test_id("console-search-input")
        locator.fill(data)

    def click_to_empty_space(self):
        self.page.query_selector("body").click()

    def click_button(self, name):
        self.page.get_by_role("button", name=name).click()

    def click_iframe_button(self, button_text):
        # self.page.wait_for_timeout(10000)
        if button_text == "Вернуться в чат-бот":
            self.page.wait_for_timeout(10000)
            self.page.frame_locator('iframe[src="https://chatbot.mts.ru"]').get_by_text(button_text).click(force=True,timeout=600000)
        else:
            self.page.frame_locator("iframe").get_by_role("button", name=button_text).last.click(timeout=120000)
        #     self.page.frame_locator('iframe').locator(f'button:has-text("{button_text}")').last.click(timeout=120000)

    def click_open_chatbot(self):
        self.page.query_selector('div.button-open').click()

    def open_first_element(self, text):
        self.page.get_by_role('cell', name=text).first.click()

    def type_in_chat(self, text):
        locator = self.page.frame_locator('iframe').get_by_role("textbox")
        locator.fill(text)
        send_button = self.page.frame_locator('iframe').get_by_title('Отправить сообщение')
        send_button.click()

    def click_cancel(self):
        cancel_button = self.page.frame_locator('iframe').get_by_title('Отмена')
        cancel_button.click()
        