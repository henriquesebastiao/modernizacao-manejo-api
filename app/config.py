from pydantic import BaseSettings


class Settings(BaseSettings):
    db_type: str
    db_user: str
    db_password: str
    db_host: str
    db_port: int
    db_name: str
    db_ssl: str

    class Config:
        env_file = ".env"


settings = Settings()
