from pydantic import BaseSettings, Field
from typing import Optional
from functools import lru_cache


class Settings(BaseSettings):
    """System configurations."""

    # system env
    ENVIRONMENT: Optional[str] = Field(None, env="ENVIRONMENT")

    # api version
    API_V1_STR = "/api/v1"

    # loading .env file
    class Config:
        env_file = ".env"
        case_sensitive = True


class DevConfig(Settings):
    """Development configurations."""

    # Mysql
    MYSQL_SERVER: Optional[str] = Field(None, env="DEV_MYSQL_SERVER")
    MYSQL_USER: Optional[str] = Field(None, env="DEV_MYSQL_USER")
    MYSQL_PASSWORD: Optional[str] = Field(None, env="DEV_MYSQL_PASSWORD")
    MYSQL_DB_NAME: Optional[str] = Field(None, env="DEV_MYSQL_DB_NAME")
    MYSQL_PORT: Optional[int] = Field(None, env="DEV_MYSQL_PORT")


class ProdConfig(Settings):
    """Development configurations."""

    # Mysql
    MYSQL_SERVER: Optional[str] = Field(None, env="PROD_MYSQL_SERVER")
    MYSQL_USER: Optional[str] = Field(None, env="PROD_MYSQL_USER")
    MYSQL_PASSWORD: Optional[str] = Field(None, env="PROD_MYSQL_PASSWORD")
    MYSQL_DB_NAME: Optional[str] = Field(None, env="PROD_MYSQL_DB_NAME")
    MYSQL_PORT: Optional[int] = Field(None, env="PROD_MYSQL_PORT")


class FactoryConfig:
    """Returns a config instance dependending on the ENV_STATE variable."""

    def __init__(self, env_state: Optional[str]):
        self.env_state = env_state

    def __call__(self):

        if self.env_state == "development":
            return DevConfig()

        elif self.env_state == "production":
            return ProdConfig()


@lru_cache()
def get_configs():
    """load env file"""
    from dotenv import load_dotenv
    load_dotenv(encoding='utf-8')
    return FactoryConfig(Settings().ENVIRONMENT)()


configs = get_configs()
