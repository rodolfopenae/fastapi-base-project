from kernel.domain.base_entity import BaseEntity
import hashlib

class User(BaseEntity):
    def __init__(self, id: int, username:str, password: str, role: str):
        self.id = id
        self.username = username
        self.password = password
        self.role= role
    
    
    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password,
            'role': self.role
        }
    
    def from_dict(self):
        return User(
            id= self.id,
            username= self.username,
            password= self.password,
            role= self.role
        )
        
    @classmethod
    def create_password(cls, password):
        hash = hashlib.md5()
        hash.update(password.encode('utf-8'))
        return hash.hexdigest()