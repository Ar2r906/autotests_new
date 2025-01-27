import logging

from api_tests.public_api_test.get_example.models.example_model import object_schema
from api_tests.public_api_test.routes import botAdmin_api_routes
from base.api import BaseClient, BaseResponseModel

logger = logging.getLogger("api_tests")


class PublicApiClient(BaseClient):

    def get_example(self, route: str, params: dict = None, schema: dict = None,
                    **kwargs) -> BaseResponseModel:
        path_template = botAdmin_api_routes["example_api"].get(route)
        if path_template is None:
            raise ValueError(f"Route '{route}' not found in 'botAdmin_api_routes'.")

        # Подстановка параметров в URL
        if params:
            path = path_template.format(**params)
        else:
            path = path_template

        return self.get(path, schema=schema, params=params, **kwargs)

    # def post_example(
    #         self, route: str, params: dict = None,
    #         schema: dict = None,
    #         json_body: dict = None,
    #         **kwargs
    # ) -> BaseResponseModel:
    #     return self.post(botAdmin_api_routes["example_api"][route], schema=schema, params=params,
    #                      json_body=json_body,
    #                      **kwargs)

    def post_example(
            self, route: str, params: dict = None,
            schema: dict = None,
            json_body: dict = None,
            files: dict = None,  # Добавляем параметр для файлов
            **kwargs
    ) -> BaseResponseModel:
        path_template = botAdmin_api_routes["example_api"].get(route)
        if path_template is None:
            raise ValueError(f"Route '{route}' not found in 'botAdmin_api_routes'.")

        # Подстановка параметров в URL
        if params:
            path = path_template.format(**params)
        else:
            path = path_template

        if files:
            # Если переданы файлы, используем их для отправки запроса
            return self.post(path, schema=schema, params=params, files=files, **kwargs)
        else:
            # Иначе используем стандартный json_body
            # headers = kwargs.get('headers', {})
            # headers['Content-Type'] = 'application/json'
            # kwargs['headers'] = headers
            return self.post(path, schema=schema, params=params, json=json_body, **kwargs)

    def delete_example(self, route: str, params: dict = None, schema: dict = None,
                       **kwargs) -> BaseResponseModel:
        path_template = botAdmin_api_routes["example_api"].get(route)
        if path_template is None:
            raise ValueError(f"Route '{route}' not found in 'botAdmin_api_routes'.")

        # Подстановка параметров в URL
        if params:
            path = path_template.format(**params)
        else:
            path = path_template

        return self.delete(path, schema=schema, params=params, **kwargs)

    def put_example(self, route: str, json_body: dict = None, params: dict = None, schema: dict = None,
                    **kwargs) -> BaseResponseModel:
        path_template = botAdmin_api_routes["example_api"].get(route)
        if path_template is None:
            raise ValueError(f"Route '{route}' not found in 'botAdmin_api_routes'.")

        # Подстановка параметров в URL
        if params:
            path = path_template.format(**params)
        else:
            path = path_template

        return self.put(path, schema=schema, params=params, json_body=json_body, **kwargs)
