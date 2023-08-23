from pydantic import BaseSettings


class Settings(BaseSettings):
    db_type: str | None
    db_user: str | None
    db_password: str | None
    db_host: str | None
    db_port: int | None
    db_name: str | None
    db_ssl: str | None
    secret_key: str | None
    algorithm: str | None
    access_token_expire_minutes: int | None

    class Config:
        env_file = '.env.dev'


settings = Settings()
