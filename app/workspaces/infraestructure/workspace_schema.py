from pydantic import BaseModel


class WorkspaceRequest(BaseModel):
    title: str
    user_id: int


class WorkspaceResponse(BaseModel):
    title: str
    user_id: int

    class Config:
        orm_mode = True