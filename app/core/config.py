from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str
    API_V1_STR: str
    API_KEY: str
    
    OLLAMA_BASE_URL: str
    MODEL_NAME: str
    TIMEOUT: float = 60.0

    class Config:
        env_file = ".env"

settings = Settings()