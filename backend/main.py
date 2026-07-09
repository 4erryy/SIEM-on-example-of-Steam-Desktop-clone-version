from fastapi import FastAPI, Request
from pydantic import BaseModel, Field

app = FastAPI()  # Одно единственное объявление app

class EventModel(BaseModel):
    event_type: str
    status: str
    message: str

# Все ваши маршруты должны быть привязаны к ЭТОМУ app
@app.post("/event")
async def handle_event(request: Request):
    data = await request.json()
    print(f"[БЭКЕНД ПРИНЯЛ]: {data}")
    return {"status": "success"}

@app.post("/login")
async def login(request: Request):
    data = await request.json()
    print(f"[БЭКЕНД ПРИНЯЛ ЛОГИН]: {data}")
    return {"status": "success", "message": "Login processed"}

@app.get("/")
async def root():
    return {"status": "online"}