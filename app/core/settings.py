from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env', env_file_encoding='utf-8', extra='ignore'
    )

    # Database
    DATABASE_URL: str

    # Application
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    ALGORITHM: str
    DEBUG: int = 0
    SECRET_KEY: str
    VERSION: str = 'dev'

    # Observability
    APP_BIND_HOST: str
    APP_NAME: str = 'app-manejo'
    APP_URL: str = 'http://localhost:8000'
    EXPOSE_PORT: int = 8000
    OTLP_GRPC_ENDPOINT: str = 'http://tempo-manejo:4317'

    # 1 - To run unit tests with Pytest
    # 0 - To deploy the application with observability
    TEST: int = 0


@lru_cache
def get_settings():
    return Settings()
