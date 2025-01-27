import os
from pathlib import Path
from typing import Optional

from dotenv import load_dotenv
from pydantic import BaseSettings, Field

load_dotenv()

USERNAME = os.getenv("CI_TESTING_USERNAME")
FIO = os.getenv("CI_TESTING_FIO")
PASSWORD = os.getenv("CI_TESTING_PASSWORD")
BEHAVE_DEBUG_ON_ERROR = os.getenv("CI_TESTING_BEHAVE_DEBUG")
SMART_SECRET = os.getenv("CI_TESTING_CLIENT_SECRET")
SMART_CLIENT = os.getenv("CI_TESTING_CLIENT_ID")
SMART_ENV = os.getenv("CI_TESTING_ENV")
DEFAULT_MOUNT_POINT = "smart-test-3t5q7"
ISSO_CLIENT_ID = os.getenv("ISSO_CLIENT_ID")
ISSO_SECRET_ID = os.getenv("ISSO_SECRET_ID")


class Settings(BaseSettings):
    """
    Класс настроек тестов.
    Все настройки подтягиваются из переменных окружения,
    или из файла .env в корне проекта
    """

    UI_SMART_BASE_URL: Optional[str] = Field(
        title="Адрес тестируемого ресурса",
        default=f"https://bot.mts.ru",
    )
    UI_SMART_TAS_URL: Optional[str] = Field(
        title="Адрес тестируемого ресурса",
        default=f"https://bot.mts.ru/",
    )
    UI_SMART_INC_URL: Optional[str] = Field(
        title="Адрес тестируемого ресурса",
        default=f"https://{SMART_ENV}.smartitsm.mts-corp.ru/incidents",
    )
    UI_SMART_CRQ_REG_URL: Optional[str] = Field(
        title="Адрес тестируемого ресурса",
        default=f"https://{SMART_ENV}.smartitsm.mts-corp.ru/changes-registration",
    )

    UI_SCREENSHOT_ENABLER: bool = Field(
        title="Флаг для специального метода скриншотов", default=False
    )
    UI_WINDOW_WIDTH: int = Field(title="Ширина окна", default=1680)
    UI_WINDOW_HEIGHT: int = Field(title="Высота окна", default=1020)

    UI_BROWSER_NAME: Optional[str] = Field(
        title="Название браузера для запуска", default="chrome"
    )
    UI_BROWSER_HEADLESS: Optional[bool] = Field(
        title="Режим запуска браузера", default=False
    )
    UI_IGNORE_INSECURE_CERTS: bool = Field(
        title="Игнорирование ошибок сертификата", default=True
    )
    ENABLE_TEST_RETRY: bool = Field(
        title="Включение механихмов ретраев тестов", default=False
    )
    PUBLIC_API_BASE_URL: Optional[str] = Field(title='Адрес ресурса',
                                                   default="https://route")
    # VAULT_URL: Optional[str] = Field(title='Адрес vault', default="https://vault.mts-corp.ru")
    # VAULT_ROLE_ID: Optional[str] = Field(title='vault role id')
    # VAULT_SECRET_ID: Optional[str] = Field(title='vault secret id')
    # VAULT_MOUNT_POINT: Optional[str] = Field(title='default vault mount point', default=DEFAULT_MOUNT_POINT)
    # VAULT_SECRET_PATH: Optional[str] = Field(title='vault secret path', default='Staging')

    ISSO_BASE_URL: Optional[str] = Field(
        title="Адрес isso", default="https://isso.mts.ru"
    )
    ISSO_CLIENT_ID: Optional[str] = Field(title="Isso client id - как логин", default=ISSO_CLIENT_ID)
    ISSO_SECRET_ID: Optional[str] = Field(title="Isso client secret - как пароль", default=ISSO_SECRET_ID)

    API_IMS_BASE_URL: Optional[str] = Field(
        title="Адрес тестируемого ресурса", default="https://manager.0001hdtest01.msk.mts.ru"
    )

    class Config:
        env_file = Path(__file__).parent / "../.env"
        env_file_encoding = "utf-8"


settings = Settings()
root_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
