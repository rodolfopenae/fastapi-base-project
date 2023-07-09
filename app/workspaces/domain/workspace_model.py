from kernel.domain.base_entity import BaseEntity

class Workspace(BaseEntity):
    def __init__(self, id: int, title: str, user_id: int):
        self.id = id
        self.title = title
        self.user_id = user_id
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'user_id': self.user_id
        }
    
    def from_dict(self):
        return Workspace(
            id= self.id,
            title= self.title,
            user_id= self.user_id,
        )
