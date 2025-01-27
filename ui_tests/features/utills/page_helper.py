from typing import cast

from playwright.sync_api import Page


def page_from(context):
    check_page(context)
    return cast(Page, context.page)


def check_page(context):
    assert hasattr(context, 'page'), 'Отсутствует объект page в контексте'
