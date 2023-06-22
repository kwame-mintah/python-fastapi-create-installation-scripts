from fastapi import APIRouter

router = APIRouter(prefix="/projects", tags=["projects"])


@router.get("/")
async def read_root() -> dict:
    return {"message": "This is the projects endpoint"}
