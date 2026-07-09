from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from backend.security.security_processor import SecurityProcessor

router = APIRouter()

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
    
    if not user or not SecurityProcessor.verify_password(payload.password, user["password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Incorrect username or password"
        )
    
    access_token = SecurityProcessor.create_access_token(data={"sub": user["username"]})
    
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }
