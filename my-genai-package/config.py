from pydantic_settings import BaseSettings,SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "groq chatbot"
    groq_api_key: str
    model: str = "qwen/qwen3.8-27b"

    model_config = SettingsConfigDict(
            env_file=".env"
    )

settings = Settings()
