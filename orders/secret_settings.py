from pydantic import BaseSettings


class Settings(BaseSettings):
    SECRET_KEY: str
    DEBUG: bool
    ALLOWED_HOSTS: str
    ENGINE: str
    NAME_DB: str
    USER: str
    PASSWORD: str
    HOST: str
    PORT: str
    CELERY_BROKER_URL: str
    CELERY_RESULT_BACKEND: str

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


settings = Settings()
