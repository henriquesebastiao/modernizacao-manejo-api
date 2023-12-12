from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    db_type: str | None
    db_user: str | None
    db_password: str | None
    db_host: str | None
    db_port: int | None
    db_name: str | None
    secret_key: str | None
    algorithm: str | None
    access_token_expire_minutes: int | None

    model_config = SettingsConfigDict(env_file='.env')


settings = Settings()
