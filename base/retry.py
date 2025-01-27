import time
from functools import wraps

from behave.contrib.scenario_autoretry import patch_scenario_with_autoretry

from base.settings import settings

"""
Функция для патча enviroment behave для автоматическиого ретрая тестов
"""


def behave_patch_retry(feature):
    if settings.ENABLE_TEST_RETRY:
        for scenario in feature.scenarios:
            if ("autoretry" in scenario.effective_tags) | ("flaky" in scenario.effective_tags):
                patch_scenario_with_autoretry(scenario, max_attempts=2)


"""
Декоратор для ретраев pytest
"""


def autoretry(stop_max_attempt_number=2, wait_fixed=5):
    def decorator(test_func_ref):
        @wraps(test_func_ref)
        def wrapper(*args, **kwargs):
            retry_count = 1
            if settings.ENABLE_TEST_RETRY:
                while retry_count < stop_max_attempt_number:
                    try:
                        return test_func_ref(*args, **kwargs)
                    except AssertionError as assert_error:
                        assert_message, _ = assert_error.__str__().split("\n")
                        print(f"Retry error: \"{test_func_ref.__name__}\" --> {assert_message}. "
                              f"[{retry_count}/{stop_max_attempt_number - 1}] Retrying new execution in {wait_fixed} second(s)")
                        time.sleep(wait_fixed)
                        retry_count += 1

            # Preserve original traceback in case assertion Failed
            return test_func_ref(*args, **kwargs)

        return wrapper

    return decorator


"""
Декоратор для ретраев pytest
"""


def flaky():
    return autoretry()
