from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "User Manager API"
    app_version: str = "v5.0.0"
    database_url: str = Field(default="postgresql+psycopg2://postgres:postgres@localhost:5432/user_manager", alias="DATABASE_URL")
    jwt_secret_key: str = Field(default="change_me_secret_key", alias="JWT_SECRET_KEY")
    jwt_algorithm: str = Field(default="HS256", alias="JWT_ALGORITHM")
    access_token_expire_minutes: int = Field(default=60, alias="ACCESS_TOKEN_EXPIRE_MINUTES")
    redis_url: str = Field(default="redis://localhost:6379/0", alias="REDIS_URL")

    model_config = SettingsConfigDict(env_file=".env", case_sensitive=False)

settings = Settings()
