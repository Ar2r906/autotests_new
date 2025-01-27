import allure
import pytest
from base.fake import random_string, random_number
from ..api import PublicApi

# class NewsApi(PublicApi):
#
#     @allure.title('Создание новости, статус 200')
#     @pytest.mark.parametrize("data", {
#
#     })
#     def test_create_news(self, base_client, base_url, endpoint, data):
#         response = base_client.post_something(base_url, endpoint, data)
#         assert response.status_code == 200

