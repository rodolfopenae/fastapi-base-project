from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated
from users.application.user_use_cases import AuthenticateUser
from users.infraestructure.user_interface import UserInterface
from kernel.infraestructure.postgres_database import session
from auth.domain.token_model import Token
from auth.infraestructure.token_schema import TokenResponse

router = APIRouter()

@router.post('/auth', response_model= TokenResponse)
async def auth(token: Annotated[OAuth2PasswordRequestForm, Depends()]):
    username = token.username
    password = token.password
    repository = UserInterface(session)
    user = AuthenticateUser(repository).execute(username, password)
    if user:
        return Token.encode(user).to_dict()
    else:
        raise HTTPException(
                status_code= 401,
                detail= "Invalid email or password",
                headers={'WWW-Authenticate': 'Bearer'}
            )
