from fastapi import APIRouter, HTTPException, status, Security
from users.infraestructure.user_schema import UserRequest, UserResponse, UserUpdateRequest
from users.domain.user_model import User
from users.application.user_use_cases import (
    AddUser, 
    GetUsers,
    GetUserById,
    RemoveUser,
    UpdateUser  
)
from users.infraestructure.user_interface import UserInterface
from kernel.infraestructure.postgres_database import session
from typing import List, Annotated
from workspaces.domain.workspace_model import Workspace
from auth.infraestructure.utils import get_current_user
from workspaces.infraestructure.workspace_interface import WorkspaceInterface
from workspaces.application.workspace_use_cases import AddWorkspace

router = APIRouter()

@router.post('/users/', response_model= UserResponse)
async def create_user(user: UserRequest) -> User:
    interface = UserInterface(session)
    user= AddUser(interface).execute(user)
    if user:
        title = user['username'] + "'s workspace"
        user_id =user['id']
        interface = WorkspaceInterface(session)
        workspace = AddWorkspace(interface).execute(title, user_id)
        return user
    else:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='Username already exists'
        )
        
@router.get('/users/', response_model=List[UserResponse])
async def get_users(current_user : Annotated[User, Security(get_current_user,scopes=['admin'] )]) -> List[User]:
    interface = UserInterface(session)
    users = GetUsers(interface).execute()
    return users

@router.get("/users/{user_id}", response_model= UserResponse)
async def get_user(user_id: str):
    interface = UserInterface(session)
    user = GetUserById(interface).execute(user_id)
    return user

@router.delete("/users/{user_id}")
async def delete_user(user_id: str):
    interface = UserInterface(session)
    user = RemoveUser(interface).execute(user_id)
    return user

@router.put("/users/{user_id}", response_model= UserResponse)
async def update_user(user_id: str, user: UserUpdateRequest):
    interface = UserInterface(session)
    user = UpdateUser(interface).execute(user_id, user)
    return user