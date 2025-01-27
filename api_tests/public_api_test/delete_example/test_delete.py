import allure
import pytest


@allure.epic("Автотесты_Public_API")
@allure.story("Example Story")
@allure.suite("example suit")
@allure.description("Метод example, return something")
class TestDelete:

    @allure.title("Delete dictionary guid, возвращает 200")
    def test_delete_dictionary_guid(self, base_client, isso_token):
        base_client.delete_example(
            route="delete_dictionary_guid",
            headers={"Authorization": isso_token},
            params={
                "guid": "2324240-eqweca-e1d32-asdadf"
            }
        ).assert_that(
            has_status=200,
            validate_model=None,
        )

    @allure.title("Delete dictionary map guid, возвращает 200")
    def test_delete_dictionary_map_guid(self, base_client, isso_token):
        base_client.delete_example(
            route="delete_dictionary_map_guid",
            headers={"Authorization": isso_token},
            params={
                "guid": "2324240-eqweca-e1d32-asdadf"
            }
        ).assert_that(
            has_status=200,
            validate_model=None,
        )

    @allure.title("Delete dictionary-catalog guid, возвращает 200")
    def test_delete_dictionary_catalog_guid(self, base_client, isso_token):
        base_client.delete_example(
            route="delete_dictionary-catalog_guid",
            headers={"Authorization": isso_token},
            params={
                "guid": "2324240-eqweca-e1d32-asdadf"
            }
        ).assert_that(
            has_status=200,
            validate_model=None,
        )

    @allure.title("Delete mapping guid, возвращает 200")
    def test_delete_mapping_guid(self, base_client, isso_token):
        base_client.delete_example(
            route="delete_mapping_guid",
            headers={"Authorization": isso_token},
            params={
                "guid": "2324240-eqweca-e1d32-asdadf"
            }
        ).assert_that(
            has_status=200,
            validate_model=None,
        )

    @allure.title("Delete mapping record guid, возвращает 200")
    def test_delete_mapping_record_guid(self, base_client, isso_token):
        base_client.delete_example(
            route="delete_mapping_record_guid",
            headers={"Authorization": isso_token},
            params={
                "guid": "2324240-eqweca-e1d32-asdadf"
            }
        ).assert_that(
            has_status=200,
            validate_model=None,
        )

    @allure.title("Delete recycle id, возвращает 200")
    def test_delete_recycle_id(self, base_client, isso_token):
        base_client.delete_example(
            route="delete_recycle_id",
            headers={"Authorization": isso_token},
            params={
                "id": 1
            }
        ).assert_that(
            has_status=200,
            validate_model=None,
        )

    @allure.title("Delete role guid, возвращает 200")
    def test_delete_role_guid(self, base_client, isso_token):
        base_client.delete_example(
            route="delete_role_guid",
            headers={"Authorization": isso_token},
            params={
                "guid": "2324240-eqweca-e1d32-asdadf"
            }
        ).assert_that(
            has_status=200,
            validate_model=None,
        )

    @allure.title("Delete recycle login, возвращает 200")
    def test_delete_recycle_login(self, base_client, isso_token):
        base_client.delete_example(
            route="delete_recycle_login",
            headers={"Authorization": isso_token},
            params={
                "login": "login"
            }
        ).assert_that(
            has_status=200,
            validate_model=None,
        )

    @allure.title("Delete tree id, возвращает 200")
    def test_delete_tree_id(self, base_client, isso_token):
        base_client.delete_example(
            route="delete_tree_id",
            headers={"Authorization": isso_token},
            params={
                "id": 2044
            }
        ).assert_that(
            has_status=200,
            validate_model=None,
        )

    @allure.title("Delete tree-catalog guid, возвращает 200")
    def test_delete_tree_catalog_guid(self, base_client, isso_token):
        base_client.delete_example(
            route="delete_tree-catalog_guid",
            headers={"Authorization": isso_token},
            params={
                "guid": "3f805a3a-5dda-447a-aa69-08dcc26a0216"
            }
        ).assert_that(
            has_status=200,
            validate_model=None,
        )
