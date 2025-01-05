from pydantic_settings import BaseSettings
from pydantic import model_validator, Field, ValidationError


class Settings(BaseSettings):
    DB_HOST: str = Field(..., env="DB_HOST")
    DB_PORT: int = Field(..., env="DB_PORT")
    DB_USER: str = Field(..., env="DB_USER")
    DB_PASSWORD: str = Field(..., env="DB_PASSWORD")
    DB_NAME: str = Field(..., env="DB_NAME")
    DATABASE_URL: str | None = None  # This field will be populated dynamically

    @model_validator(mode="after")
    def set_database_url(self):
        self.DATABASE_URL = (
            f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}"
            f"@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )
        return self

    class Config:
        env_file = ".env"


settings = Settings()
