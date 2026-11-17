from functools import lru_cache

from dotenv import load_dotenv
from pydantic import Field, PostgresDsn, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()

class ProductDBSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8', extra='ignore')

    PRODUCT_DB_DNS: PostgresDsn
    PSQL_USER: str = Field(min_length=3)
    PSQL_PASSWORD: SecretStr
    PSQL_PORT: int = Field(gt=0)
    PSQL_HOST: str = Field(min_length=4)

    @classmethod
    def get_psql_password(cls) -> str:
        return cls.PSQL_PASSWORD.get_secret_value()

@lru_cache(maxsize=1)
def get_product_settings() -> ProductDBSettings:
    return ProductDBSettings()
