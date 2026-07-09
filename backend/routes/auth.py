from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from backend.security.security_processor import SecurityProcessor

# Оставляем роутер без префикса, как было изначально в проекте
router = APIRouter()

# Имитация БД пользователей
USERS_DB = {
    "admin": {
        "username": "admin",
        "password": SecurityProcessor.hash_password("admin123")
    }
}


class LoginRequest(BaseModel):
    username: str
    password: str


@router.post("/login")
def login(payload: LoginRequest):
    user = USERS_DB.get(payload.username)

    # Проверка пользователя и пароля через наш SecurityProcessor
    if not user or not SecurityProcessor.verify_password(payload.password, user["password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Неверное имя пользователя или пароль"
        )

    # Генерируем настоящий JWT-токен
    access_token = SecurityProcessor.create_access_token(data={"sub": user["username"]})

    # Возвращаем стандартный формат OAuth2
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }