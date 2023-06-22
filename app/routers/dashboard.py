from fastapi import APIRouter

router = APIRouter(prefix="/dashboard", tags=["dashboard"])


@router.get("/")
async def read_root() -> dict:
    return {"message": "This is the dashboard endpoint"}
