from fastapi import APIRouter
from backend.core.event_center import EventCenter

router = APIRouter()
center = EventCenter()

@router.post("/event")
def event(data: dict):
    center.emit("event", data)
    return {"ok": True}