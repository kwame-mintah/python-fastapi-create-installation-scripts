from fastapi import APIRouter, Depends

from app.services.setting_service import SettingService

router = APIRouter(prefix="/settings", tags=["settings"])


def get_setting_service():
    return SettingService


@router.get("/")
async def get_settings(
    service: SettingService = Depends(get_setting_service()),
) -> dict:
    return service.return_stub_data()


@router.put("/update")
async def update_settings(
    service: SettingService = Depends(get_setting_service()),
) -> dict:
    return service.return_stub_data()
