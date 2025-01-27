import os

import pytest
import allure
import requests
from dotenv import load_dotenv

load_dotenv()

class TestApiPostArticles:

    base_url = os.getenv('BASE_URL')
    test_url = os.getenv('TEST_URL')

    @allure.title('Создание статьи, статус 201')
    @pytest.mark.api
    @pytest.mark.parametrize('data', [
        ({'title': 'Заголовок1', 'content': 'Контент1', 'image': None}),
        ({'title': 'Заголовок2', 'content': 'Контент2', 'image': './sss/ss.jpg'}),
        ({'title': 'Заголовок3', 'content': 'Контент3', 'image': './sss/ss/ss/ss.png'}),
    ])
    def test_create_article(self, data):
        headers = {
            "Content-Type": "application/json"
        }

        response = requests.post(f'{self.test_url}/articles/create_article', json=data, headers=headers)
        response_json = response.json()
        delete_id = int(response_json['id'])

        print(f"Response status code: {response.status_code}")
        print(f"Response content: {response.text}")

        assert response.status_code == 201

        delete_response = requests.delete(f'{self.test_url}/articles/delete_article/{delete_id}')
        delete_response_json = delete_response.json()
        print(delete_response_json)
        assert delete_response.status_code == 204
