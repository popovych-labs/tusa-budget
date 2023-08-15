from typing import Any, Optional, Union

from pydantic import PostgresDsn, AnyUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=('dev.env', 'prod.env'), 
        env_file_encoding='utf-8',
        extra='ignore',
    )

    db_url: Union[PostgresDsn, AnyUrl, None] = None
    db_connect_args: dict[str, Any] = {}


settings = Settings()
