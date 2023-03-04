from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRES_MINUTES: int
    API_KEY: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

# pyright: reportGeneralTypeIssues=false
settings = Settings()

