import os


class Config:
    HOST = os.getenv("HOST", "127.0.0.1")
    PORT = int(os.getenv("PORT", 8000))

    # Параметры безопасности
    SECRET_KEY = os.getenv("SECRET_KEY", "super-secret-key-change-in-production-12345")
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30  # Токен сгорает через 30 минут


settings = Config()