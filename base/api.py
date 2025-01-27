import json
import types
from typing import Callable, Any
import pytest_check as check

import allure
import requests
from allure_commons.types import AttachmentType
from jsonschema.validators import validate
from pydantic import ValidationError
from requests import Response

from base.assert_helpers import check_same_json
from base.settings import settings
from base.utils import get_content_by_type, read_file_with_encoding


class BaseResponseModel:
    def __init__(self, status: int, data=None, headers: dict = None, formatted_response: dict | list = None):
        self.status = status
        self.data = data
        self.headers = headers
        self.formatted_response = formatted_response

    def is_equals(self,
                  expected_data=None,
                  expected_data_path=None,
                  transform_expected_func: Callable[[Any], Any] = None,
                  transform_response_func: Callable[[Any], Any] = None,
                  **kwargs):
        raise NotImplementedError

    def contains(self,
                 expected_data=None,
                 expected_data_path: str = None,
                 transform_expected_func: Callable[[Any], Any] = None,
                 transform_response_func: Callable[[Any], Any] = None,
                 **kwargs):
        raise NotImplementedError

    @allure.step("Assert response")
    def assert_that(self,
                    has_status: int = None,
                    is_equals: Any = None,
                    is_equals_file: str = None,
                    contains: Any = None,
                    not_empty: bool = None,
                    transform_expected_func: Callable[[Any], Any] = None,
                    transform_response_func: Callable[[Any], Any] = None,
                    additional_asserts: list = None,
                    validate_model=None,
                    list_key: str = "items",
                    **kwargs
                    ):
        if has_status:
            check.equal(self.status, has_status, "Response code status not equals expected")
        if is_equals or is_equals_file:
            self.is_equals(is_equals, is_equals_file, transform_expected_func, transform_response_func, **kwargs)
        if contains:
            self.contains(contains, transform_expected_func, transform_response_func, **kwargs)
        if not_empty:
            check.is_true(self.data, "Response body is Empty")
        if additional_asserts:
            for condition in additional_asserts:
                message = None
                if isinstance(condition, tuple):
                    assert len(condition) in {1, 2}, "Tuple conditions must have length 1 or 2"
                    condition, message = condition[0], condition[1] if len(condition) == 2 else None

                if isinstance(condition, types.FunctionType):
                    check.is_true(condition(self), msg=message)
                else:
                    check.is_true(condition, msg=message)
        if validate_model:
            try:
                if isinstance(self.data, list | str) and list_key:
                    data = {list_key: self.data}
                else:
                    data = self.data
                validate_model(**data)
            except ValidationError as e:
                check.is_true(False, f"Validation failed with error: {str(e)}")
        return self


class JsonResponseModel(BaseResponseModel):
    def __init__(self, status: int, data: dict = None, headers: dict = None, formatted_response=None):
        super().__init__(status, data, headers, formatted_response)

    def is_equals(self,
                  expected_data: dict = None,
                  expected_data_path: str = None,
                  transform_expected_func: Callable[[Any], Any] = None,
                  transform_response_func: Callable[[Any], Any] = None,
                  ignore_fields: set = ()):
        response_json = self.data
        if expected_data_path:
            json_file = read_file_with_encoding(expected_data_path)
            expected_data = json.loads(json_file)
        elif not expected_data:
            raise RuntimeError("Expected result not found")

        if transform_expected_func:
            expected_data = transform_expected_func(expected_data)
        if transform_response_func:
            response_json = transform_response_func(response_json)

        check_same_json(response_json, expected_data, ignore_fields)


class BaseClient:

    def __init__(self, base_url: str, **kwargs):
        self.base_url = base_url
        self.kwargs = kwargs

    def custom_request(self, method: str = "POST", rout: str = "", schema: dict = None,
                       attach_response_flag: bool = False, **kwargs) -> BaseResponseModel:
        url = f"{self.base_url}{rout}"
        with ((allure.step(f"{method} {url}"))):
            attach_request(method, url, **kwargs)

            response = requests.request(method, url, verify=False, **kwargs)

            content_type = response.headers.get('Content-Type')
            content_data, attach_type = get_content_by_type(content_type, response)
            formatted_data = json.dumps(content_data, indent=4, ensure_ascii=False).replace(
                "null", "None").replace("false", "False").replace("true", "True")
            if attach_response_flag:
                attach_response(content_data, response.status_code, response.headers, attach_type)
            if schema:
                validate(instance=content_data, schema=schema)
            match attach_type:
                case AttachmentType.JSON:
                    return JsonResponseModel(status=response.status_code, data=content_data, headers=response.headers,
                                             formatted_response=formatted_data)

    def post(self, rout: str = "", **kwargs) -> BaseResponseModel:
        return self.custom_request("POST", rout, **kwargs)

    def get(self, rout: str = "", **kwargs) -> BaseResponseModel:
        return self.custom_request("GET", rout, **kwargs)

    def put(self, rout: str = "", **kwargs) -> BaseResponseModel:
        return self.custom_request("PUT", rout, **kwargs)

    def delete(self, rout: str = "", **kwargs) -> BaseResponseModel:
        return self.custom_request("DELETE", rout, **kwargs)


def get_isso_token(isso_client_id=settings.ISSO_CLIENT_ID, isso_secret_id=settings.ISSO_SECRET_ID) -> str:
    grant_type = 'client_credentials'

    sso_data = {'grant_type': grant_type,
                'client_id': isso_client_id,
                'client_secret': isso_secret_id,
                'scope': "botmanager-dev"}

    client = BaseClient(settings.ISSO_BASE_URL)
    headers = {'accept': '*/*', 'Content-Type': 'application/x-www-form-urlencoded'}
    response = client.post("/auth/realms/mts/protocol/openid-connect/token", data=sso_data, headers=headers)
    return f"Bearer {response.data['access_token']}"


def attach_response(response: Response):
    with allure.step(f"Response {response.status_code}"):
        allure.attach(response.content, name="response", attachment_type=AttachmentType.TEXT)
        allure.attach(str(response.headers), name="headers", attachment_type=AttachmentType.JSON)


def attach_request(method, url, **kwargs):
    with allure.step(f"{method} {url}"):
        for k, v in kwargs.items():
            if kwargs.get(k) is not None:
                allure.attach(str(kwargs.get(k)), name=k, attachment_type=AttachmentType.TEXT)


class ResponseModel:
    def __init__(self, status: int, response: dict = None, headers: dict = None):
        self.status = status
        self.response = response
        self.headers = headers
