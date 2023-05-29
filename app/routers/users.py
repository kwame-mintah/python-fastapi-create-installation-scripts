from fastapi import APIRouter

router = APIRouter(prefix="/user", tags=["user"],
                   responses={
                       404: {"description": "Not found"}
                   })


@router.get("/")
async def read_root() -> dict:
    return {"message": "Hello, can you users see this?"}
