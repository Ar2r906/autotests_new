import hvac
from hvac import Client

from base.settings import settings


class VaultConnector(Client):

    def __init__(self, url: str = settings.VAULT_URL, vault_role_id: str = settings.VAULT_ROLE_ID,
                 vault_secret_id: str = settings.VAULT_SECRET_ID, mount_point: str = None, path: str = None, **kwargs):
        super().__init__(url, **kwargs)
        self.url = url
        self.vault_role_id = vault_role_id
        self.vault_secret_id = vault_secret_id
        self.vault_secret_id = vault_secret_id
        self.mount_point = mount_point
        self.path = path

    def get_client_by_app_role(self):
        vault_client = hvac.Client(url=self.url, verify=False)
        vault_client.auth.approle.login(
            role_id=self.vault_role_id,
            secret_id=self.vault_secret_id,
        )
        return vault_client

    def list_secrets(self, mount_point: str = None, path: str = None):
        if not mount_point:
            mount_point = self.mount_point
            if not mount_point:
                raise VaultEngineReadingException("Vault mount point not set")

        if not path:
            path = self.path
            if not path:
                raise ValueError("Vault Path is required")

        return self.get_client_by_app_role().secrets.kv.v2.read_secret(path=path, mount_point=mount_point)['data'][
            'data']


class VaultEngineReadingException(Exception):
    pass
