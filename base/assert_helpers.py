import difflib

import allure
from allure_commons.types import AttachmentType
from jsondiff import diff as json_diff
from lxml import etree
from pytest_check import check

from base.utils import try_parse_json_to_string, get_diff_xml, ignore_json_keys


def check_same_json(actual: dict, expected: dict, ignore_fields: set = ()):
    cleaned_actual = ignore_json_keys(actual, ignore_fields)
    cleaned_expected = ignore_json_keys(expected, ignore_fields)
    #TODO: Если cleaned_actual = {}, то сравнение не вызовет diff.
    difference = json_diff(cleaned_expected, cleaned_actual, syntax='explicit', marshal=True)
    difference_pretty, diff_type = try_parse_json_to_string(difference)
    if difference_pretty:
        allure.attach(difference_pretty, name="Difference", attachment_type=diff_type)

    if len(difference) > 2000:
        difference = difference[:2000]
    check.is_true(not difference, f"Actual not equals expected. Difference: \n{difference}")


def get_difference_strings(actual, expected):
    matcher = difflib.SequenceMatcher(None, actual, expected)
    difference = []

    for opcode, i1, i2, j1, j2 in matcher.get_opcodes():
        if opcode == 'equal':
            continue
        if opcode in ['delete', 'replace']:
            diff_str = f'- actual[{i1}:{i2}]: {actual[i1:i2]}'
            difference.append(diff_str)
        if opcode in ['insert', 'replace']:
            diff_str = f'+ expected[{j1}:{j2}]: {expected[j1:j2]}'
            difference.append(diff_str)

    return difference

def check_same_string(actual: str, expected: str):
    difference = get_difference_strings(actual, expected)

    if difference:
        difference_pretty, diff_type = try_parse_json_to_string(difference)
        allure.attach(difference_pretty, name="Difference", attachment_type=diff_type)

    if len(difference) > 2000:
        difference = difference[:2000]
    check.is_true(not difference, f"Actual not equals expected. Difference: \n{difference}")


def check_same_xml(actual: etree, expected: etree):
    response_difference = get_diff_xml(actual, expected)

    if len(response_difference) > 2000:
        response_difference = response_difference[:2000]

    if response_difference:
        allure.attach(response_difference, name="Response Difference", attachment_type=AttachmentType.TEXT)
    check.is_true(not response_difference, f"Actual not equals expected. Difference: \n{response_difference}")
