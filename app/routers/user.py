from fastapi import APIRouter, Depends

from app.services.user_service import UserService

router = APIRouter(
    prefix="/user", tags=["user"], responses={404: {"description": "User not found"}}
)


def get_user_service():
    return UserService


@router.get("/")
async def read_root() -> dict:
    return {"message": "This is the users endpoint"}


@router.get("/{identifier}/details")
async def get_user_details(
    identifier: str, service: UserService = Depends(get_user_service())
) -> dict:
    print(identifier)
    return service.return_stub_data()
