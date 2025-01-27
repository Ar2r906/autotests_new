import logging

from behave import *
from playwright._impl._errors import TimeoutError
from playwright.sync_api import expect

from base.settings import FIO, PASSWORD, USERNAME, settings
from ui_tests.features.pages.base_page import BasePage
from ui_tests.features.pages.locators.base_locators import BasePageLocators
from ui_tests.features.pages.locators.TAS_locators import TasPageLocators
from ui_tests.features.pages.main_page import SmartMainPage
from ui_tests.features.pages.tas_page import TasPage
from ui_tests.features.pages.web_sso_login import WebSSOLoginPage
from ui_tests.features.utills.logging.logger import get_logger
from ui_tests.features.utills.page_helper import check_page, page_from
from ui_tests.features.utills.screenshoter import enabledScreenshotCtx

logger = get_logger()


@step("Перейти по ссылке на страницу '{page}'")
def step_impl(context, page):
    """Шаг переходит по указанному адресу продукта"""
    check_page(context)
    if page == "Задачи":
        page_from(context).goto(settings.UI_SMART_TAS_URL, timeout=40000)
    elif page == "Инциденты":
        page_from(context).goto(settings.UI_SMART_INC_URL, timeout=40000)
    elif page == "Регистрация CRQ":
        page_from(context).goto(settings.UI_SMART_CRQ_REG_URL, timeout=40000)
    else:
        page_from(context).goto(settings.UI_SMART_BASE_URL, timeout=40000)
        logger.warning("URL не передан, открыта главная страница")
    enabledScreenshotCtx(context)
    logger.warning("Перейти по ссылке")


@step("Пользователь проходит авторизацию")
def step_impl(context):
    web_sso_page = WebSSOLoginPage(page_from(context))
    enabledScreenshotCtx(context)
    web_sso_page.login_user(user_name=USERNAME, password=PASSWORD)
    enabledScreenshotCtx(context)
    logger.info("Пользователь проходит авторизацию")


@step("Пользователь автоматически залогинен")
def step_impl(context):
    locators = BasePageLocators(context.page)
    username = locators.get_user_name()
    expect(username).to_contain_text(FIO)
    logger.info("Пользователь автоматически залогинен")


@step('Активна консоль "{console}"')
def step_impl(context, console):
    locators = BasePageLocators(context.page)
    if not console:
        logging.info("Не получено название консоли")
    locator = locators.console_tas
    expect(locator).to_contain_text(console)
    main_page = SmartMainPage(page_from(context))
    main_page.wait_page_loaded("load")
    logger.info(f'Активна консоль "{console}"')


@step('Открываем вкладку с текстом "{text}"')
def step_impl(context, text):
    check_page(context)
    base = BasePage(page_from(context))
    base.find_by_text(text)
    logger.info(f'Открываем вкладку с текстом "{text}"')


@step("Активна страница '{page}'")
def step_impl(context, page):
    check_page(context)
    main_page = BasePage(page_from(context))
    main_page.wait_page_loaded("load")
    if page == "Задачи":
        main_page.check_current_url_is(settings.UI_SMART_TAS_URL)
    elif page == "Инциденты":
        main_page.check_current_url_is(settings.UI_SMART_BASE_URL)
    elif page == "Регистрация CRQ":
        main_page.check_current_url_is(settings.UI_SMART_CRQ_REG_URL)
    logger.info("Открывается главная страница")


@step('Ввести в поиск "{data}"')
def step_impl(context, data):
    main_page = BasePage(page_from(context))
    main_page.fill_search_field(data)
    logger.info(f'Ввести в поиск "{data}"')


@step('Кликнуть по столбцу "{text}"')
def step_impl(context, text):
    locators = TasPageLocators(context.page)
    locators.find_console_row(text)
    logger.info(f'Кликнуть по полю "{text}"')


@step('Кликнуть на чекбокс "{rowname}"')
def step_impl(context, rowname):
    locators = TasPageLocators(context.page)
    locators.find_checkbox_by_row_name(rowname).click()
    logger.info(f'Кликнуть на чекбокс "{rowname}"')


@step('Выбрать значение "{text}"')
def step_impl(context, text):
    page = BasePage(page_from(context))
    context.page.get_by_test_id("table_tasks_list").get_by_role("list").get_by_text(
        text
    ).click()
    context.page.get_by_text("Применить").click()
    page.wait_page_loaded()
    logger.info(f"Выбрать значение '{text}'")


@step('В столбце отображаются элементы с фильтром "{text}"')
def check_column_data(context, text: str):
    """
    :param context: Playwright context object.
    :param text: Ожидаемый текст в столбце.
    Проверяет, что количество найденных элементов с выбранным фильтром == количеству отображаемых записей.
    """
    locators = BasePageLocators(context.page)
    table = context.page.query_selector(".table")
    count = 0
    for _ in table.query_selector_all(f':text-is("{text}")'):
        count += 1
    try:
        elements_on_page = int(locators.get_elements_count())
    except TimeoutError:
        elements_on_page = 0
    assert (
        elements_on_page == count
    ), f"Expected count={elements_on_page}, actual count={count}"
    logger.info(elements_on_page)


@step('Кликнуть в таблице на первый элемент "{text}"')
def step_impl(context, text):
    page = BasePage(page_from(context))
    page.wait_page_loaded()
    page.open_first_element(text)
    page.wait_page_loaded()


@step('Карточка в статусе "{status}"')
def step_impl(context, status):
    locators = BasePageLocators(context.page)
    page = BasePage(page_from(context))
    page.wait_page_loaded()
    status_on_page = locators.get_card_status(status).inner_text()
    assert status in status_on_page, logger.warning(
        f"Expected status={status}, actual status={status_on_page}",
    )


@step('Изменить назначенное лицо на "{operator}"')
def step_impl(context, operator):
    locators = BasePageLocators(context.page)
    page = TasPage(page_from(context))
    current_operator = locators.get_user_name().inner_text()
    page.fill_operator_field(current_operator)
    context.page.locator(".reassignRow").click()  # первая карточка в поиске
    page.wait_page_loaded()


@step('Назначенное лицо "{operator}"')
def step_impl(context, operator):
    locators = BasePageLocators(context.page)
    page = TasPage(page_from(context))
    page.wait_page_loaded()
    operator_username = locators.get_operator_name().inner_text()
    current_user_name = locators.get_user_name().inner_text()
    if operator == "Текущий оператор":
        assert operator_username == current_user_name
    if operator == "Другой оператор":
        assert operator_username != current_user_name, logger.warning(
            f"Текущий оператор - {current_user_name}"
        )
    if operator == "Не назначено":
        assert operator_username == operator
