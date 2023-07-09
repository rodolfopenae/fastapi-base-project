from kernel.domain.base_repository import BaseRepository
from workspaces.domain.workspace_model import Workspace
from .workspace_table import WorkspaceTable
from typing import List

class WorkspaceInterface(BaseRepository):
    def __init__(self, session) -> None:
        self.session = session
    
    def add(self, title: str, user_id: int) -> Workspace:
        try:
            workspace = WorkspaceTable(
                title = title,
                user_id = user_id
            )
            self.session.add(workspace)
            self.session.commit()
        except Exception as exception:
            raise NameError(
                f'An error was ocurred, checkout {exception}'
            )

    def list(self) -> List[Workspace]:
        try:
            workspaces = self.session.query(WorkspaceTable).all()
            return [
                Workspace(
                    id = workspace.id,
                    title = workspace.title,
                    user_id = workspace.user_id
                ).to_dict()
                for workspace in workspaces
            ]
        except Exception as exception:
            raise NameError(
                f'An error was ocurred, checkout {exception}'
            )

    def remove():
        ...

    def update():
        ...


    
    def get():
        ...
    
    def commit(self):
        return self.session.commit()