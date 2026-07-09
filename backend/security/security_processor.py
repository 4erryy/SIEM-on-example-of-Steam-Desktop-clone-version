from datetime import datetime, timedelta, timezone
import jwt
import bcrypt
from backend.config import settings

class SecurityProcessor:
    @staticmethod
    def hash_password(password: str) -> str:
        """Хеширование пароля с солью с помощью чистого bcrypt"""
        pwd_bytes = password.encode('utf-8')
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(pwd_bytes, salt)
        return hashed.decode('utf-8')

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        """Сравнение пароля с хэшем"""
        try:
            pwd_bytes = plain_password.encode('utf-8')
            hashed_bytes = hashed_password.encode('utf-8')
            return bcrypt.checkpw(pwd_bytes, hashed_bytes)
        except Exception:
            return False

    @staticmethod
    def create_access_token(data: dict) -> str:
        """Создание JWT токена"""
        to_encode = data.copy()
        expire = datetime.now(timezone.utc) + timedelta(minutes=getattr(settings, "ACCESS_TOKEN_EXPIRE_MINUTES", 30))
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=getattr(settings, "ALGORITHM", "HS256"))
        return encoded_jwt

    @staticmethod
    def decode_access_token(token: str) -> dict | None:
        """Проверка JWT токена"""
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[getattr(settings, "ALGORITHM", "HS256")])
            return payload
        except jwt.PyJWTError:
            return None
