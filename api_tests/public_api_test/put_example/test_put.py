import allure
import pytest


@allure.epic("Автотесты_Public_API")
@allure.story("Example Story")
@allure.suite("example suit")
@allure.description("Метод example, return something")
class TestPut:

    @allure.title("Put mapping guid, return 200")
    def test_put_mapping_guid(self, base_client, isso_token):
        base_client.put_example(
            route="put_mapping_guid",
            headers={"Authorization": isso_token},
            params={
                "guid": "2324240-eqweca-e1d32-asdadf"
            },
            json_body={"value": "string",
                       "mappingRecordGuid": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                       "type": 0}
        ).assert_that(
            has_status=200,
            validate_model=None,
        )

    @allure.title("Put role guid roleId, return 200")
    def test_put_role_guid_roleId(self, base_client, isso_token):
        base_client.put_example(
            route="put_role_guid_roleId",
            headers={"Authorization": isso_token},
            params={
                "guid": "2324240-eqweca-e1d32-asdadf",
                "roleId": 1
            }
        ).assert_that(
            has_status=200,
            validate_model=None,
        )
