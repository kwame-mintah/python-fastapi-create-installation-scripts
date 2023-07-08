from fastapi import APIRouter, Depends
from fastapi.responses import FileResponse

from app.services.projects_service import ProjectsService

router = APIRouter(prefix="/projects", tags=["projects"])


def get_project_service():
    return ProjectsService


@router.get("/")
async def get_projects(
    service: ProjectsService = Depends(get_project_service()),
) -> dict:
    return service.return_stub_data()


@router.get("/{identifier}/details")
async def get_project_details(
    identifier: str, service: ProjectsService = Depends(get_project_service())
) -> dict:
    return service.return_stub_data_id(identifier)


@router.post("/{identifier}/details/{os}")
async def download_project_script(
    identifier: str, os: str, service: ProjectsService = Depends(get_project_service())
) -> FileResponse:
    return service.return_stub_data_software_packages(identifier, os)
