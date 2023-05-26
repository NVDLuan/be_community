from typing import Any
from typing import Dict
from typing import Optional

from pydantic import BaseSettings
from pydantic import PostgresDsn
from pydantic import validator


class Settings(BaseSettings):
    DEBUG: Optional[bool] = False
    SQLALCHEMY_DEBUG: bool = False
    POSTGRES_SERVER: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_PORT: str
    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = None
    SECRET_KEY: Optional[str] = None
    EXPIRE_TOKEN: Optional[int] = 0

    CLOUD_NAME: Optional[str] = None
    API_KEY: Optional[str] = None
    API_SECRET: Optional[str] = None

    EMAIL: Optional[str] = None
    PASSWORD_EMAIL: Optional[str] = None

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql",
            user=values.get("POSTGRES_USER"),
            password=values.get("POSTGRES_PASSWORD"),
            host=values.get("POSTGRES_SERVER"),
            path=f"/{values.get('POSTGRES_DB') or ''}",
            query=values.get("POSTGRES_SCHEMA"),
            port=values.get("POSTGRES_PORT"),
        )


settings = Settings(_env_file='.env', _env_file_encoding='utf-8')
