from kernel.application.base_use_case import BaseUseCase
from kernel.domain.base_repository import BaseRepository
from workspaces.domain.workspace_model import Workspace


class AddWorkspace(BaseUseCase):
    def __init__(self, repo: BaseRepository) -> None:
        self.repo = repo
    
    def execute(self, title: str, user_id: int) -> Workspace:
        with self.repo as repo:
            return repo.add(title, user_id)

class RemoveWorkspace(BaseUseCase):
    ...

class UpdateWorkspace(BaseUseCase):
    ...

class GetWorkspaces(BaseUseCase):
    def __init__(self, repo: BaseRepository) -> None:
        self.repo = repo
    
    def execute(self) -> Workspace:
        with self.repo as repo:
            return repo.list()

class GetWorkspaceById(BaseUseCase):
    ...
