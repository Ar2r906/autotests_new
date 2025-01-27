import pytest

from api_tests.public_api_test.api import PublicApiClient
from base.api import get_isso_token
from base.settings import settings


@pytest.fixture(scope="class")
def base_client() -> PublicApiClient:
    return PublicApiClient(settings.API_IMS_BASE_URL)

@pytest.fixture
def isso_token() -> str:
    return get_isso_token()

@pytest.fixture
def cleanup_resources(base_client):
    created_resources = []
    def register_resources(resources_type, resource_id):
        created_resources.append((resources_type, resource_id))

    yield register_resources

    for resources_type, resource_id in created_resources:
        base_client.delete_example(
            route=f"delete_{resources_type}",
            params={"id": resource_id}
        )