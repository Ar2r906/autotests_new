import requests
import os
import pytest
import allure
from dotenv import load_dotenv

load_dotenv()

class TestApiGetArticles:

    base_url = os.getenv('BASE_URL')
    test_url = os.getenv('TEST_URL')

    @allure.title('Получение всех статей, статус 200')
    @pytest.mark.api
    def test_get_articles(self):
        response = requests.get(f"{self.test_url}/articles")
        assert response.status_code == 200, f"Ожидался код 200, получен {response.status_code}"

        response_json = response.json()
        #print(response_json)
        assert response_json is not None, f"Ожидался True, получен {response_json}"

    @allure.title("Получение статьи по id, статус 200")
    @pytest.mark.api
    @pytest.mark.parametrize("id", [7, 3, 6, 5])
    def test_get_article_by_id(self, id):
        response = requests.get(f"{self.test_url}/articles/{id}")
        assert response.status_code == 200, f"Ожидался 200, получен {response.status_code}"

        response_json = response.json()
        assert int(response_json["id"]) == id, f"Ожидался {id}, полуен {response_json["id"]}"

    @allure.title("Получение статьи по некорректному id, статус 413")
    @pytest.mark.api
    @pytest.mark.parametrize("id", ([13.44, 'sdty', -19, 0, '&*()', ' ']))
    def test_get_articles_invalid_id(self, id):
        response = requests.get(f"{self.test_url}/articles/{id}")
        assert response.status_code == 413, f"Ожидалось 404, получена {response.status_code}"

        response_json = response.json()
        assert response_json == {'error': 'Введите корректный id'}, f"Ожидалось пустое тело ответа, получено {response_json}"