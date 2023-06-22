from fastapi import APIRouter

router = APIRouter(
    prefix="/user", tags=["user"], responses={404: {"description": "User not found"}}
)


@router.get("/")
async def read_root() -> dict:
    return {"message": "This is the users endpoint"}
