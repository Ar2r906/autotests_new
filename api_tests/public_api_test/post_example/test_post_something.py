import allure
import pytest

#
#
#

@allure.epic("Автотесты_Public_API")
@allure.story("Example Story")
@allure.suite("example suit")
@allure.description("Метод example, return something")
class TestPostExample:

    # @allure.title("Title")
    # @pytest.mark.parametrize(
    #     "some_id, date",
    #     [
    #         ("1", "2024-04-15T06:10:25.553Z",),
    #     ]
    # )
    # def test_post_example(self, base_client, isso_token, some_id, date):
    #     params = {
    #         "some_id": some_id,
    #         "date": date,
    #     }
    #     base_client.post_example(
    #         route="post_example",
    #         headers={"Authorization": isso_token},
    #         json_body=params,
    #     ).assert_that(
    #         has_status=200,
    #     )

    @allure.title("Post dictionary, return 200")
    @pytest.mark.parametrize(
        "name, dictionaryCatalogGuid",
        [
            ("Example Dictionary", "3fa85f64-5717-4562-b3fc-2c963f66afa6"),
        ]
    )
    def test_post_dictionary(self, base_client, isso_token, name, dictionaryCatalogGuid):
        params = {
            "name": name,
            "dictionaryCatalogGuid": dictionaryCatalogGuid,
        }
        base_client.post_example(
            route="post_dictionary",
            headers={"Authorization": isso_token},
            json_body=params,
        ).assert_that(
            has_status=200,
        )

    @allure.title("Post dictionary map, return 200")
    @pytest.mark.parametrize(
        "dictionary_guid, catalog_guid",
        [
            ("123e4567-e89b-12d3-a456-426614174000", "123e4567-e89b-12d3-a456-426614174001"),
        ]
    )
    def test_post_dictionary_map(self, base_client, isso_token, dictionary_guid, catalog_guid):
        params = {
            "dictionaryGuid": dictionary_guid,
            "catalogGuid": catalog_guid,
        }
        base_client.post_example(
            route="post_dictionary_map",
            headers={"Authorization": isso_token},
            json_body=params,
        ).assert_that(
            has_status=200
        )

    @allure.title("Save tree dictionary changes, return 200")
    @pytest.mark.parametrize(
        "tree_id, changes",
        [
            (1, [{"changeType": 0, "guid": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                  "dictionaryGuid": "3fa85f64-5717-4562-b3fc-2c963f66afa6", "value": "example"}]),
        ]
    )
    def test_post_dictionary_tree(self, base_client, isso_token, tree_id, changes):
        base_client.post_example(
            route="post_dictionary_tree_treeId",
            headers={"Authorization": isso_token},
            params={"treeId": tree_id},
            json_body=changes,
        ).assert_that(
            has_status=200
        )

    @allure.title("Add tree catalog, return 200")
    @pytest.mark.parametrize(
        "parent_catalog_guid, name",
        [
            ("123e4567-e89b-12d3-a456-426614174000", "New Catalog"),
        ]
    )
    def test_post_dictionary_catalog(self, base_client, isso_token, parent_catalog_guid, name):
        params = {
            "parentGuid": parent_catalog_guid,
            "name": name,
        }
        base_client.post_example(
            route="post_dictionary-catalog",
            headers={"Authorization": isso_token},
            json_body=params,
        ).assert_that(
            has_status=200
        )

    @allure.title("Post dictionary-catalog rename, return 200")
    @pytest.mark.parametrize(
        "catalog_guid, new_name",
        [
            ("123e4567-e89b-12d3-a456-426614174000", "Renamed Catalog"),
        ]
    )
    def test_post_dictionary_catalog_guid_rename_name(self, base_client, isso_token, catalog_guid, new_name):
        base_client.post_example(
            route="post_dictionary-catalog_guid_rename_name",
            params={"guid": catalog_guid, "name": new_name},
            headers={"Authorization": isso_token},
        ).assert_that(
            has_status=200
        )

    @allure.title("Post mapping, return 200")
    @pytest.mark.parametrize(
        "value, mappingRecordGuid, type",
        [
            ("string", "3fa85f64-5717-4562-b3fc-2c963f66afa6", 0),
        ]
    )
    def test_post_mapping(self, base_client, isso_token, value, mappingRecordGuid, type):
        params = {
            "valur": value,
            "mappingRecordGuid": mappingRecordGuid,
            "type": type
        }
        base_client.post_example(
            route="/api/mapping",
            headers={"Authorization": isso_token},
            json_body=params,
        ).assert_that(
            has_status=200
        )

    @allure.title("Post mapping record dictionaryGuid, return 200")
    @pytest.mark.parametrize(
        "dictionary_guid",
        [
            ("123e4567-e89b-12d3-a456-426614174000"),
        ]
    )
    def test_post_mapping_record_dictionaryGuid(self, base_client, isso_token, dictionary_guid):
        base_client.post_example(
            route="post_mapping_record_dictionaryGuid",
            headers={"Authorization": isso_token},
            params={"dictionaryGuid": dictionary_guid}
        ).assert_that(
            has_status=200
        )

    @allure.title("Post recycle id restore, return 200")
    @pytest.mark.parametrize(
        "scenario_id",
        [
            1,
        ]
    )
    def test_post_recycle_id_restore(self, base_client, isso_token, scenario_id):
        base_client.post_example(
            route="post_recycle_id_restore",
            headers={"Authorization": isso_token},
            params={"id": scenario_id}
        ).assert_that(
            has_status=200
        )

    @allure.title("Post role catalogGuid, return 200")
    @pytest.mark.parametrize(
        "catalog_guid, user_info",
        [
            ("123e4567-e89b-12d3-a456-426614174000", {"guid": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                                                      "login": "string",
                                                      "name": "string",
                                                      "roleId": 0}),
        ]
    )
    def test_post_role_catalogGuid(self, base_client, isso_token, catalog_guid, user_info):
        base_client.post_example(
            route="post_role_catalogGuid",
            params={"catalogGuid": catalog_guid},
            headers={"Authorization": isso_token},
            json=user_info
        ).assert_that(
            has_status=200
        )

    @allure.title("Post tree import, return 200")
    @pytest.mark.parametrize(
        "scenarios",
        [
            ([{
                "id": 0,
                "name": "string",
                "description": "string",
                "treeCatalogGuid": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                "nodes": [
                    {
                        "id": 0,
                        "guid": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                        "parentNode": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                        "priority": 0,
                        "line": "string",
                        "prompt": "string",
                        "descendantPrompt": "string",
                        "action": 0,
                        "parameter": "string",
                        "fixedValue": "string",
                        "fieldGuid": "string"
                    }
                ]
            }]),
        ]
    )
    def test_post_tree_import(self, base_client, isso_token, scenarios):
        base_client.post_example(
            route="post_tree_import",
            headers={"Authorization": isso_token},
            json=scenarios
        ).assert_that(
            has_status=200
        )

    @allure.title("Post tree id copy, return 200")
    @pytest.mark.parametrize(
        "scenario_id",
        [
            1,
        ]
    )
    def test_post_tree_id_copy(self, base_client, isso_token, scenario_id):
        base_client.post_example(
            route="post_tree_id_copy",
            headers={"Authorization": isso_token},
            params={"id": scenario_id}
        ).assert_that(
            has_status=200
        )

    @allure.title("Post tree, return 200")
    def test_post_tree(self, base_client, isso_token):
        params = {"id": 0}
        # {
        #       "id": 2044,
        #       "name": "Undeletable tree",
        #       "description": "",
        #       "treeCatalogGuid": "064626ee-e7e9-42f1-aa62-08dcc26a0216",
        #       "nodes": [
        #         {
        #           "id": 34420,
        #           "guid": "5775c603-e2f5-4e15-988e-db2327a75924",
        #           "parentNode": None,
        #           "priority": 0,
        #           "line": "",
        #           "prompt": "",
        #           "descendantPrompt": "",
        #           "action": 1,
        #           "parameter": "",
        #           "fixedValue": "",
        #           "fieldGuid": ""
        #         }
        #       ]
        #     }
        base_client.post_example(
            route="post_tree",
            headers={"Authorization": isso_token},
            json_body=params
        ).assert_that(
            has_status=200
        )

    @allure.title("Post tree-catalog, return 200")
    @pytest.mark.parametrize(
        "new_section",
        [
            ({
                "parentGuid": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                "name": "string"
            }),
        ]
    )
    def test_post_tree_catalog(self, base_client, isso_token, new_section):
        base_client.post_example(
            route="post_tree-catalog",
            headers={"Authorization": isso_token},
            json=new_section
        ).assert_that(
            has_status=200
        )

    @allure.title("Post tree-catalog guid rename newName, return 200")
    @pytest.mark.parametrize(
        "guid, new_name",
        [
            ("123e4567-e89b-12d3-a456-426614174000", "Renamed Catalog"),
        ]
    )
    def test_post_tree_catalog_guid_rename_newName(self, base_client, isso_token, guid, new_name):
        base_client.post_example(
            route="post_tree-catalog_guid_rename_newName",
            headers={"Authorization": isso_token},
            params={"guid": guid, "new_name": new_name}
        ).assert_that(
            has_status=200
        )

    @allure.title("Post utility uploadfile, return 200")
    @pytest.mark.parametrize(
        "file_path",
        [
            ("./test.txt"),  # Укажите путь к вашему тестовому файлу
        ]
    )
    def test_post_utility_uploadfile(self, base_client, isso_token, file_path):
        with open(file_path, 'rb') as file:
            file_content = file.read()
            file_name = file_path.split('/')[-1]

            base_client.post_example(
                route="post_utility_uploadfile",
                headers={"Authorization": isso_token},
                files={
                    "FileName": (None, file_name),
                    "FormFile": (file_name, file_content, "application/octet-stream")
                }
            ).assert_that(
                has_status=200
            )
            