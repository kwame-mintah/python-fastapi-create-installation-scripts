from fastapi import APIRouter

router = APIRouter(prefix="/settings", tags=["settings"])


@router.get("/")
async def read_root() -> dict:
    return {"message": "This is the settings endpoint"}
