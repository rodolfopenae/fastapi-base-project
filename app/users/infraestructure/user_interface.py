from kernel.domain.base_repository import BaseRepository
from users.domain.user_model import User
from .user_table import UserTable
from workspaces.infraestructure.workspace_table import WorkspaceTable
from typing import List

class UserInterface(BaseRepository):
    def __init__(self, session) -> None:
        self.session = session
    
    def add(self, user: User)->User:
        try:
            user_in_db = self.session.query(UserTable).filter(UserTable.username == user.username).first()
            if not user_in_db:
                user = UserTable(
                    username = user.username,
                    password = User.create_password(user.password),
                    role = user.role
                )
                self.session.add(user)
                self.session.commit()
                return User(
                    id = user.id,
                    username= user.username,
                    password= user.password,
                    role= user.role
                    ).to_dict()
            else:
                return user
        except Exception as exception:
            raise NameError(
                f'An error was ocurred, checkout {exception}'
            )
    
        
    def list(self) -> List[User]:
        try:
            users = self.session.query(UserTable).all()
            return [
                User(
                    id = user.id,
                    username = user.username,
                    password = user.password,
                    role=user.role
                ).to_dict()
                for user in users
            ]
        except Exception as exception:
            raise NameError(
                f'An error was ocurred, checkout {exception}'
            )
    
    def authenticate(self, username: str, password: str) -> User:
        try:
            user_in_db = self.session.query(UserTable).filter(UserTable.username == username).first()
            if user_in_db and User.create_password(password) == user_in_db.password:
                return user_in_db
        except Exception as exception:
            raise NameError(
                f'An error was ocurred, checkout {exception}'
            )
            
    def get(self, user_id: str) -> User:
        try:
            user = self.session.query(UserTable).filter(UserTable.id == user_id).first()
            return User(
                id = user.id,
                username = user.username,
                password = user.password,
                role=user.role
            ).to_dict()
        except Exception as exception:
            raise NameError(
                f'An error was ocurred, checkout {exception}'
            )
    def remove(self, user_id: str)-> User:
        try:
            user = self.session.query(UserTable).filter(UserTable.id == user_id).first()
            self.session.delete(user)
            self.session.commit()
            return {
                "user was succesufully removed"
            }
            
        except Exception as exception:
            raise NameError(
                f'An error was ocurred, checkout {exception}'
            )
    
    def update(self, user_id: str, user: User) -> User:
        try:
            user_db = self.session.query(UserTable).filter(UserTable.id == user_id).first()
            user_db.password = User.create_password(user.password)
            self.commit()
            return User(
                id = user_db.id,
                username = user_db.username,
                password = user_db.password,
                role=user_db.role
            ).to_dict()
        except Exception as exception:
            raise NameError(
                f'An error was ocurred, checkout {exception}'
            )
    
    def commit(self):
        return self.session.commit()
