import allure
from allure_commons.types import AttachmentType
from playwright.sync_api import Page

from base.settings import settings
from ui_tests.features.utills.page_helper import page_from


def screenshot(page: Page, name='Screenshot'):
    print(page)
    allure.attach(page.screenshot(), name=name, attachment_type=AttachmentType.PNG)


def screenshotCtx(context, name='Screenshot'):
    screenshot(page_from(context), name=name)


def enabledScreenshotCtx(context, name='Screenshot'):
    enabledScreenshot(page_from(context), name)


def enabledScreenshot(page: Page, name='Screenshot'):
    if settings.UI_SCREENSHOT_ENABLER:
        screenshot(page, name)
