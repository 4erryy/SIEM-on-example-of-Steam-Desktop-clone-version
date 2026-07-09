from fastapi import APIRouter

router = APIRouter()

users = []

@router.get("/users")
def get_users():
    return users