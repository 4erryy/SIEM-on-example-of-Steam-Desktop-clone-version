import os


class Config:
    # Базовые настройки сервера
    HOST = os.getenv("HOST", "127.0.0.1")
    PORT = int(os.getenv("PORT", 8000))

    # Настройки безопасности и авторизации
    SECRET_KEY = os.getenv("SECRET_KEY", "super-secret-key-change-in-production")
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30

    # Интеграция с Агентом
    AGENT_TOKEN = os.getenv("AGENT_TOKEN", "default_agent_secret_token")

class Settings:
    SECRET_KEY = "SUPER_SECRET_KEY_KEEP_IT_SAFE"  # Можно изменить на любой сложный текст
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30

settings = Settings()