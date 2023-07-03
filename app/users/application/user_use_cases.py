from kernel.domain.base_entity import BaseEntity
from kernel.application.base_use_case import BaseUseCase
from kernel.domain.base_repository import BaseRepository
from ..domain.user_model import User


class AddUser(BaseUseCase):
    def __init__(self, repo: BaseRepository) -> None:
        self.repo = repo
    
    def execute(self, user: User) -> User:
        with self.repo as repo:
            return repo.add(user)

class GetUsers(BaseUseCase):
    def __init__(self, repo: BaseRepository) -> None:
        self.repo = repo
    
    def execute(self) -> bool:
        with self.repo as repo:
            return repo.list()

class AuthenticateUser(BaseUseCase):
    def __init__(self, repo: BaseRepository) -> None:
        self.repo = repo
    
    def execute(self, username, password) -> bool:
        with self.repo as repo:
            return repo.authenticate(username, password)
        
class GetUserById(BaseUseCase):
    def __init__(self, repo: BaseRepository) -> None:
        self.repo = repo
    
    def execute(self, user_id: str) -> BaseEntity:
        with self.repo as repo:
            return repo.get(user_id)

class RemoveUser(BaseUseCase):
    def __init__(self, repo: BaseRepository) -> None:
        self.repo = repo
    
    def execute(self, user_id: str) -> BaseEntity:
        with self.repo as repo:
            return repo.remove(user_id)
        
class UpdateUser(BaseUseCase):
    def __init__(self, repo: BaseRepository) -> None:
        self.repo = repo
    
    def execute(self, user_id: str, user: User) -> BaseEntity:
        with self.repo as repo:
            return repo.update(user_id, user)