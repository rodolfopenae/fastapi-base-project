from fastapi import APIRouter
from workspaces.application.workspace_use_cases import GetWorkspaces
from workspaces.infraestructure.workspace_interface import WorkspaceInterface
from kernel.infraestructure.postgres_database import session

router = APIRouter()

@router.get('/workspaces')
async def get_workspaces():
    interface = WorkspaceInterface(session)
    workspaces = GetWorkspaces(interface).execute()
    return workspaces

