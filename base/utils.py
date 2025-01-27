import json
import os.path

from allure_commons.types import AttachmentType
from lxml import etree
from xmldiff import main as xml_diff, formatting
from xmldiff.formatting import WS_BOTH

from base.settings import root_dir


def get_diff_xml(observed, expected):
    formatter = formatting.XmlDiffFormatter(normalize=WS_BOTH)
    differ = xml_diff.diff_texts(observed, expected, formatter=formatter)
    return differ


def ignore_xml_elements(xml, tags_to_ignore):
    for tag in tags_to_ignore:
        elements = xml.findall('.//{}'.format(tag))
        for element in elements:
            parent = element.getparent()
            if parent is not None:
                parent.remove(element)
    return xml


def ignore_json_keys(d: dict, keys: set):
    if isinstance(d, list):
        return [ignore_json_keys(x, keys) for x in d]
    elif isinstance(d, dict):
        return {k: v if not isinstance(v, dict) else ignore_json_keys(v, keys)
                for k, v in d.items() if k not in keys}


def keys_to_str(input_dict):
    if isinstance(input_dict, dict):
        return {str(key): keys_to_str(value) for key, value in input_dict.items()}
    elif isinstance(input_dict, list):
        return [keys_to_str(element) for element in input_dict]
    else:
        return input_dict


def try_parse_json_to_string(response_content):
    try:
        return json.dumps(response_content, indent=4, ensure_ascii=False), AttachmentType.JSON
    except:
        try:
            return json.dumps(json.load(response_content), indent=4, ensure_ascii=False), AttachmentType.JSON
        except:
            return response_content, AttachmentType.TEXT


def try_parse_xml(response_text):
    try:
        return etree.fromstring(response_text), AttachmentType.XML
    except etree.XMLSyntaxError:
        return try_parse_json_to_string(response_text)


def get_content_by_type(content_type, response):
    if content_type is None:
        data, content_type = try_parse_xml(response.text)
    elif 'application/json' in content_type:
        data = response.json()  # для json ответа
        content_type = AttachmentType.JSON
    elif 'application/xml' in content_type:
        data = etree.fromstring(response.content)  # для xml ответа
        content_type = AttachmentType.XML
    else:
        data = response.text  # для строкового ответа
        content_type = AttachmentType.TEXT
    return data, content_type


def read_file_with_encoding(file_path, encodings: set = ('utf-8-sig', 'utf-8', 'latin-1')):
    for encoding in encodings:
        try:
            with open(os.path.join(root_dir, file_path), encoding=encoding) as file:
                return file.read()
        except UnicodeDecodeError:
            pass
    raise ValueError(f"Unable to decode file: {file_path}")
