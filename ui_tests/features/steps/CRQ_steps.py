from datetime import datetime, timedelta

from behave import *
from playwright.sync_api import expect

from ui_tests.features.pages.CRQ_page import CrqPage
from ui_tests.features.utills.logging.logger import get_logger
from ui_tests.features.utills.page_helper import check_page, page_from
from ui_tests.features.utills.screenshoter import screenshot

logger = get_logger()


@step("Кликнуть кнопку Отмена")
def step_impl(context):
    check_page(context)
    crq_page = CrqPage(page_from(context))
    crq_page.wait_page_loaded("load")
    crq_page.click_cancel()


@step("Кликнуть кнопку '{button_text}'")
def step_impl(context, button_text):
    check_page(context)
    crq_page = CrqPage(page_from(context))
    crq_page.wait_page_loaded("load")
    crq_page.click_iframe_button(button_text)


@step("Кликнуть на кнопку чатбота")
def step_impl(context):
    check_page(context)
    crq_page = CrqPage(page_from(context))
    crq_page.wait_page_loaded("load")
    crq_page.click_open_chatbot()
    crq_page.wait_page_loaded()


@step("Ввести в чат {text}")
def step_impl(context, text):
    check_page(context)
    crq_page = CrqPage(page_from(context))
    crq_page.wait_page_loaded("load")
    crq_page.type_in_chat(text)
    crq_page.wait_page_loaded()


@step("Ввести в поле ИТ-Система '{it_system}'")
def step_impl(context, it_system):
    check_page(context)
    crq_page = CrqPage(page_from(context))
    crq_page.wait_page_loaded("load")
    crq_page.choose_it_system(it_system)
    crq_page.find_by_role("link", name=it_system, exact=True).click()


@step("Выбрать тип изменения '{change_type}'")
def step_impl(context, change_type):
    check_page(context)
    crq_page = CrqPage(page_from(context))
    crq_page.wait_page_loaded("load")
    crq_page.choose_change_type(change_type)


@step("Выбрать влияние '{impact}'")
def step_impl(context, impact):
    check_page(context)
    crq_page = CrqPage(page_from(context))
    crq_page.wait_page_loaded("load")
    crq_page.choose_impact(impact)


@step("Заполнить описание '{description}'")
def step_impl(context, description):
    check_page(context)
    crq_page = CrqPage(page_from(context))
    crq_page.wait_page_loaded("load")
    crq_page.fill_description(description)


@step("Ввести даты")
def step_impl(context):
    check_page(context)
    crq_page = CrqPage(page_from(context))
    crq_page.wait_page_loaded("load")
    crq_page.fill_date()
    crq_page.click_to_empty_space()


@step("Выставить значение '{text}' '{option}'")
def step_impl(context, text, option):
    check_page(context)
    crq_page = CrqPage(page_from(context))
    crq_page.wait_page_loaded("load")
    crq_page.choose_checkbox(text, option)


@step("Заполнить поле Информация о тестировании '{testing_description}'")
def step_impl(context, testing_description):
    check_page(context)
    crq_page = CrqPage(page_from(context))
    crq_page.wait_page_loaded("load")
    crq_page.fill_testing_description(testing_description)


@step("Заполнить поле План возврата '{return_plan}'")
def step_impl(context, return_plan):
    check_page(context)
    crq_page = CrqPage(page_from(context))
    crq_page.wait_page_loaded("load")
    crq_page.fill_return_plan(return_plan)


@step("Заполнить поле Основание для изменения '{change_description}'")
def step_impl(context, change_description):
    check_page(context)
    crq_page = CrqPage(page_from(context))
    crq_page.wait_page_loaded("load")
    crq_page.fill_change_description(change_description)


@step(
    "Под названием '{role}' кликнуть кнопку и заполнить поля '{first_arg}' '{second_arg}' '{third_arg}'"
)
def step_impl(context, role, first_arg, second_arg, third_arg):
    check_page(context)
    crq_page = CrqPage(page_from(context))
    crq_page.wait_page_loaded("load")
    crq_page.fill_form(role, first_arg, second_arg, third_arg)


@step("Кликнуть на кнопку '{name}'")
def step_impl(context, name):
    check_page(context)
    crq_page = CrqPage(page_from(context))
    crq_page.wait_page_loaded("load")
    crq_page.click_button(name)


@step("Появилось модальное окно '{text}'")
def step_impl(context, text):
    check_page(context)
    crq_page = CrqPage(page_from(context))
    crq_page.wait_page_loaded("load")
    crq_page.locators.crq_reg_modal.is_visible(timeout=10000)
    expect(crq_page.locators.crq_reg_modal).to_contain_text(text, timeout=10000)


@step("Номер CRQ из модального окна отображается в консоли")
def step_impl(context):
    check_page(context)
    crq_page = CrqPage(page_from(context))
    crq_page.wait_page_loaded("load")
    context.saved_crq_num = crq_page.locators.crq_modal_number.inner_text()
    crq_page.click_button("Закрыть")
    expect(
        context.page.get_by_role("cell", name="CRQ").first.filter(
            has_text=context.saved_crq_num
        )
    )


@step("Дата выставляется на час вперед в плановом окончании")
def step_impl(context):
    check_page(context)
    crq_page = CrqPage(page_from(context))
    crq_page.wait_page_loaded("load")
    start = datetime.now() + timedelta(hours=1)
    crq_page.locators.date_start.type(start.strftime("%d.%m.%Y %H:%M"))
    crq_page.locators.date_end.type(start.strftime("%d.%m.%Y %H:%M"))
    date = str(start.strftime("-%m-%d"))
    context.page.get_by_title(date).click()
    crq_page.locators.description_field.click()
    screenshot(page_from(context))
