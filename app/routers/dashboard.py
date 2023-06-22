from fastapi import APIRouter, Depends

from app.services.dashboard_service import DashboardService

router = APIRouter(prefix="/dashboard", tags=["dashboard"])


def get_dashboard_service():
    return DashboardService


@router.get("/")
async def get_dashboard_properties(
    service: DashboardService = Depends(get_dashboard_service()),
) -> dict:
    return service.return_stub_data()
