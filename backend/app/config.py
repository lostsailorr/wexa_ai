import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional


class Settings(BaseSettings):
    # CognoDB / Neo4j Connection Settings
    COGNODB_URI: str = os.getenv("COGNODB_URI", os.getenv("NEO4J_URI", "bolt://localhost:7687"))
    COGNODB_USER: str = os.getenv("COGNODB_USER", os.getenv("NEO4J_USERNAME", "cognodb"))
    COGNODB_PASSWORD: str = os.getenv("COGNODB_PASSWORD", os.getenv("NEO4J_PASSWORD", ""))
    
    # Application Settings
    APP_NAME: str = "SentinelGraph - Graph Intelligence & AML Platform"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = os.getenv("DEBUG", "False").lower() in ("true", "1", "yes")
    
    # Server Settings
    PORT: int = int(os.getenv("PORT", "8000"))
    HOST: str = os.getenv("HOST", "0.0.0.0")

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )


settings = Settings()
