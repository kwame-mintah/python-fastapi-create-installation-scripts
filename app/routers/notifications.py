from fastapi import APIRouter, Depends

from app.services.notifications_service import NotificationService

router = APIRouter(prefix="/notification", tags=["notification"])


def get_notification_service():
    return NotificationService


@router.get("/")
async def get_notifications(
    service: NotificationService = Depends(get_notification_service()),
) -> dict:
    return service.return_stub_data()
