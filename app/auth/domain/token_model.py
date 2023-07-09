from kernel.domain.base_entity import BaseEntity
from users.domain.user_model import User
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv
from jose import jwt
load_dotenv()


security_secret_key = os.getenv('SECURITY_SECRET_KEY')
security_algorithm = os.getenv('SECURITY_ALGORITHM')
security_access_token_expiration_days = int(os.getenv('SECURITY_ACCESS_TOKEN_EXPIRATION_DAYS'))

class Token(BaseEntity):
    
    def __init__(self, access_token: str, token_type: str):
        self.access_token = access_token
        self.token_type = token_type

    @classmethod
    def encode(cls, user: User):
        id = user.id
        username = user.username
        role = user.role
        token = {
            'id': id,
            'username': username,
            'role': role,
            'exp': datetime.utcnow() + timedelta(days=security_access_token_expiration_days)
        }
        token_encoded = jwt.encode(
            token, 
            security_secret_key, 
            algorithm = security_algorithm
            )
        return cls(access_token=token_encoded, token_type='Bearer')
    
    def decode(token: str):
        try:
            return jwt.decode(
                token, 
                security_secret_key, 
                algorithms=[security_algorithm]
                )
        except Exception as err:
            return err
    
    def to_dict(self):
        return {
            'access_token': self.access_token,
            'token_type': self.token_type
        }
    
    def from_dict(self):
        return Token(
            access_token=self.access_token,
            token_type= self.token_type
        )