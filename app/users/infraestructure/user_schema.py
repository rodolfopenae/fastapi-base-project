from pydantic import BaseModel, Field
from ..domain.role_model import Role


class UserRequest(BaseModel):
    username: str = Field(example='rodo')
    password: str = Field(example='112233')
    role: Role = Field(example='admin')


class UserResponse(BaseModel):
    username: str
    id: int
    
    class Config:
        orm_mode = True
        allow_population_by_field_name = True

class UserUpdateRequest(BaseModel):
    password: str = Field(example='112233')