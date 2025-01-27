import allure
import pytest
import os
import requests
from dotenv import load_dotenv

load_dotenv()

class TestApiGetNews:

    base_url = os.getenv("BASE_URL")
    @pytest.mark.api
    @allure.title("Получение всех новостей, статус 200")
    def test_get_news(self):
        response = requests.get(f"{self.base_url}/news")
        print(f"{self.base_url}/news")
        assert response.status_code == 200, f"Ожидался статус 200, получен {response.status_code}"

        response_json = response.json()
        #print(response_json)
        assert response_json is not None, f"Ожидалось True, получено {response_json is not None}"

    @allure.title("Получение новости по id, статус 200")
    @pytest.mark.api
    @pytest.mark.parametrize("id", ([31, 32, 33]))
    def test_get_news_by_id(self, id):
        response = requests.get(f"{self.base_url}/news/{id}")
        response_json = response.json()
        assert response.status_code == 200, f"Ожидалось 200, получена {response.status_code}"
        assert int(response_json['id']) == id, f"Ожидался id {id}, получен {int(response_json[id])}"

    @allure.title("Получение новости по некорректному id, статус 404")
    @pytest.mark.api
    @pytest.mark.parametrize("id", (['str', 0, 1.8, -12]))
    def test_get_news_by_id_not_found(self, id):
        response = requests.get(f"{self.base_url}/news/{int(id)}")
        assert response.status_code == 404, f"Ожидалось 404, получена {response.status_code}"

        response_json = response.json()
        assert response_json == {'error': 'news not found'}, f"Ожидалось пустое тело ответа, получено {response_json}"