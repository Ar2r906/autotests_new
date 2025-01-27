import allure
import pytest

from api_tests.public_api_test.get_example.expected import expected_values
from api_tests.public_api_test.get_example.models.example_model import ModelList
from base.fakers import random_number


@allure.epic("Автотесты_Public_API")
@allure.story("Example Story")
@allure.suite("example suit")
@allure.description("Метод example, return something")
class TestGetExample:

    @allure.title("Get recycle, возвращает 200")
    # @pytest.mark.parametrize("some_id",
    #                          ["1",
    #                           "2",
    #                           "3"]
    #                          )
    def test_get_recycle(self, base_client, isso_token):
        base_client.get_example(
            route="get_recycle",
            headers={"Authorization": isso_token}
            # params={
            #     "systemId": some_id
            # }
        ).assert_that(
            has_status=200,
            # is_equals=expected_values[some_id],
            validate_model=None,
        )
        # print(perem.formatted_response, perem.status)

    @allure.title("Get recycle count, возвращает 200")
    def test_get_recycle_count(self, base_client, isso_token):
        base_client.get_example(
            route="get_recycle_count",
            headers={"Authorization": isso_token}
        ).assert_that(
            has_status=200,
            validate_model=None,
        )

    @allure.title("Get tree hd templates, возвращает 200")
    def test_get_tree_hd_templates(self, base_client, isso_token):
        base_client.get_example(
            route="get_tree_hd_templates",
            headers={"Authorization": isso_token}
        ).assert_that(
            has_status=200,
            validate_model=None,
        )

    @pytest.mark.parametrize("tree_id", ["1", "2", "3"])
    @allure.title("Get tree id chat, возвращает 200")
    def test_get_tree_id_chat(self, base_client, isso_token, tree_id):
        base_client.get_example(
            route="get_tree_id_chat",
            params={"id": tree_id},
            headers={"Authorization": isso_token}
        ).assert_that(
            has_status=200,
            validate_model=None,
        )

    @pytest.mark.parametrize("tree_guid", ["1", "2", "3"])
    @allure.title("Get tree guid chat, возвращает 200")
    def test_get_tree_guid_chat(self, base_client, isso_token, tree_guid):
        base_client.get_example(
            route="get_tree_guid_chat",
            params={"guid": tree_guid},
            headers={"Authorization": isso_token}
        ).assert_that(
            has_status=200,
            validate_model=None,
        )

    @pytest.mark.parametrize("tree_id", ["2044",])
    @allure.title("Get tree, возвращает 200")
    def test_get_tree(self, base_client, isso_token, tree_id):
        response = base_client.get_example(
            route="get_tree",
            params={"id": tree_id},
            headers={"Authorization": isso_token}
        ).assert_that(
            has_status=200,
            validate_model=None,
        )
        print(response.data['nodes'][0]['id'])

    @allure.title("Get tree export, возвращает 200")
    def test_get_tree_export(self, base_client, isso_token):
        base_client.get_example(
            route="get_tree_export",
            params={"treeIds": "1"},
            headers={"Authorization": isso_token}
        ).assert_that(
            has_status=200,
            validate_model=None,
        )

    @allure.title("Get tree catalog, возвращает 200")
    def test_get_tree_catalog(self, base_client, isso_token):
        perem = base_client.get_example(
            route="get_tree-catalog",
            headers={"Authorization": isso_token}
        ).assert_that(
            has_status=200,
            validate_model=None,
        )
        print(perem.formatted_response)

    @allure.title("Get tree catalog root, возвращает 200")
    def test_get_tree_catalog_root(self, base_client, isso_token):
        base_client.get_example(
            route="get_tree-catalog_root",
            headers={"Authorization": isso_token}
        ).assert_that(
            has_status=200,
            validate_model=None,
        )

    @pytest.mark.parametrize("role_guid", ["1", "2", "3"])
    @allure.title("Get role guid, возвращает 200")
    def test_get_role_guid(self, base_client, isso_token, role_guid):
        base_client.get_example(
            route="get_role_guid",
            params={"guid": role_guid},
            headers={"Authorization": isso_token}
        ).assert_that(
            has_status=200,
            validate_model=None,
        )

    @allure.title("Get role admin, возвращает 200")
    def test_get_role_admin(self, base_client, isso_token):
        base_client.get_example(
            route="get_role_admin",
            headers={"Authorization": isso_token}
        ).assert_that(
            has_status=200,
            validate_model=None,
        )

    @allure.title("Get role login all, возвращает 200")
    def test_get_role_login_all(self, base_client, isso_token):
        base_client.get_example(
            route="get_role_login_all",
            params={"login": "sa-chatbot-test"},
            headers={"Authorization": isso_token}
        ).assert_that(
            has_status=200,
            validate_model=None,
        )

    @allure.title("Get mapping dictionaryguid list, возвращает 200")
    def test_get_mapping_dictionaryguid_list(self, base_client, isso_token):
        base_client.get_example(
            route="get_mapping_dictionaryguid_list",
            params={"dictionaryGuid": "askpof-qwe23r-23r2e-dafsdf",
                    "query": "hello"},
            headers={"Authorization": isso_token}
        ).assert_that(
            has_status=200,
            validate_model=None,
        )

    @allure.title("Get keyword guid list, возвращает 200")
    def test_get_keyword_guid_list(self, base_client, isso_token):
        base_client.get_example(
            route="get_keyword_guid_list",
            params={"guid": "askpof-qwe23r-23r2e-dafsdf",
                    "phrase": "hello"},
            headers={"Authorization": isso_token}
        ).assert_that(
            has_status=200,
            validate_model=None,
        )

    @allure.title("Get keyword area list, возвращает 200")
    def test_get_keyword_area_list(self, base_client, isso_token):
        base_client.get_example(
            route="get_keyword_area_list",
            params={"area": "Imya",
                    "phrase": "hello"},
            headers={"Authorization": isso_token}
        ).assert_that(
            has_status=200,
            validate_model=None,
        )

    @allure.title("Get keyword area, возвращает 200")
    def test_get_keyword_area(self, base_client, isso_token):
        base_client.get_example(
            route="get_keyword_area",
            params={"area": "Imya",
                    "phrase": "hello"},
            headers={"Authorization": isso_token}
        ).assert_that(
            has_status=200,
            validate_model=None,
        )

    @allure.title("Get dictionary-catalog, возвращает 200")
    def test_get_dictionary_catalog(self, base_client, isso_token):
        base_client.get_example(
            route="get_dictionary-catalog",
            headers={"Authorization": isso_token}
        ).assert_that(
            has_status=200,
            validate_model=None,
        )

    @pytest.mark.parametrize("treeId", ["1", "2", "3"])
    @allure.title("Get dictionary_tree_treeid, возвращает 200")
    def test_get_tree_dictionary_tree_treeid(self, base_client, isso_token, treeId):
        base_client.get_example(
            route="get_dictionary_tree_treeid",
            params={"treeId": treeId},
            headers={"Authorization": isso_token}
        ).assert_that(
            has_status=200,
            validate_model=None,
        )

    @allure.title("Get dictionary, возвращает 200")
    def test_get_dictionary(self, base_client, isso_token):
        base_client.get_example(
            route="get_dictionary",
            headers={"Authorization": isso_token}
        ).assert_that(
            has_status=200,
            validate_model=None,
        )

    @allure.title("Get dictionary guid, возвращает 200")
    def test_get_dictionary_guid(self, base_client, isso_token):
        base_client.get_example(
            route="get_dictionary_guid",
            params={"guid": "derqer-sdfwef234-rwefsdfw-23413"},
            headers={"Authorization": isso_token}
        ).assert_that(
            has_status=200,
            validate_model=None,
        )