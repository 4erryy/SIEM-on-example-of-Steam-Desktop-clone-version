from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from backend.security.security_processor import SecurityProcessor

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = SecurityProcessor.decode_access_token(token)
    if not payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return payload

@router.get("/check")
def check_system_status(current_user: dict = Depends(get_current_user)):
    """Эндпоинт принимает GET-запрос и проверяет авторизацию"""
    return {
        "status": "secure",
        "message": f"Welcome, {current_user.get('sub')}. System is fully operational."
    }
