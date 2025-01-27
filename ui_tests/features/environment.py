from behave import fixture, use_fixture
from playwright.sync_api import sync_playwright, ViewportSize

from base.retry import behave_patch_retry
from base.settings import *
# from base.vault import VaultConnector
from ui_tests.features.utills.screenshoter import screenshot


@fixture
def browser_runner(context):
    print("Start Fixture")
    playwright = sync_playwright().start()
    match settings.UI_BROWSER_NAME:
        case 'firefox':
            browser = playwright.firefox.launch(headless=settings.UI_BROWSER_HEADLESS, slow_mo=500)
        case 'webKit':
            browser = playwright.webkit.launch(headless=settings.UI_BROWSER_HEADLESS, slow_mo=500)
        case 'edge':
            browser = playwright.chromium.launch(channel="msedge", headless=settings.UI_BROWSER_HEADLESS, slow_mo=500)
        case _:
            browser = playwright.chromium.launch(headless=settings.UI_BROWSER_HEADLESS, slow_mo=500)

    context.browser = browser
    # context.vault_secrets = VaultConnector().list_secrets(mount_point=settings.VAULT_MOUNT_POINT,
    #                                                       path=settings.VAULT_SECRET_PATH)
    print("End Fixture")


def get_feature_label(feature):
    """
    Предполагается, что метки теста хранятся в списке тегов объекта feature.
    Этот код может измениться в зависимости от того, как вы организуете свои тесты.
    """
    layer_label_prefix = 'allure.label.layer:'
    # print(f"Feature tags: {feature.tags}")  # Строка для отладки
    for tag in feature.tags:  # предполагает, что метки хранятся в свойстве тегов объекта feature
        if tag.startswith(layer_label_prefix):
            return tag[len(layer_label_prefix):]
    return None


def before_feature(context, feature):
    layer = get_feature_label(feature)
    if layer == 'UI':
        use_fixture(browser_runner, context)
    elif layer is None:
        raise Exception('Отсутствует метка layer для функции')
    else:
        raise Exception(f'Неизвестная метка layer: {layer}')
    # Доп логика для ретраев тестов
    behave_patch_retry(feature)
    # print("END Feature hook")
    # for scenario in feature.scenarios:
    #     if "REGRESSION" in scenario.effective_tags:
    #         patch_scenario_with_autoretry(scenario, max_attempts=3)


def before_scenario(context, scenario):
    browser_context = context.browser.new_context(ignore_https_errors=settings.UI_IGNORE_INSECURE_CERTS,
                                                  screen=ViewportSize(width=settings.UI_WINDOW_WIDTH,
                                                                      height=settings.UI_WINDOW_HEIGHT))
    page = browser_context.new_page()
    context.browser_context = browser_context
    context.page = page


def after_step(context, step):
    # Проверяем, есть ли ошибки во время выполнения тестов
    if step.status == 'failed':
        try:
            screenshot(context.page, "ScreenshotFailed")
        except Exception as e:
            print(f"Failed to attach screenshot: {str(e)}")



def after_scenario(context, scenario):
    context.page.close()


def after_feature(context, feature):
    context.browser.close()
