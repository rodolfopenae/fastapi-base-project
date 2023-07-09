from fastapi import HTTPException, status
from auth.domain.token_model import Token
from users.domain.user_model import User
from pydantic import ValidationError
from jose import JWTError
from sqlalchemy import select
from fastapi.security import OAuth2PasswordBearer, SecurityScopes
from fastapi import Depends
from users.infraestructure.user_table import UserTable

oauth2_schema = OAuth2PasswordBearer(
    tokenUrl='/auth/',
    scopes={}
    )

def get_current_user(security_scopes: SecurityScopes,token: str = Depends(oauth2_schema))-> User:
    if security_scopes:
        authenticate_value = f'Bearer scope={security_scopes.scope_str}'
    else:
        authenticate_value = 'Bearer'
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": authenticate_value}
        )
    try:
        payload = Token.decode(token)
        username: str = payload['username']
        if username is None:
            raise credentials_exception
        token_scope: str = payload['role']
        if token_scope in security_scopes.scopes:
            return select(UserTable).where(UserTable.id == payload['id'])
        else:
            raise credentials_exception
    except (JWTError, ValidationError):
        raise credentials_exception