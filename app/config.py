from pydantic import BaseSettings


class Settings(BaseSettings):
    db_type: str | None
    db_user: str | None
    db_password: str | None
    db_host: str | None
    db_port: int | None
    db_name: str | None
    db_ssl: str | None

    class Config:
        env_file = ".env"


settings = Settings()
