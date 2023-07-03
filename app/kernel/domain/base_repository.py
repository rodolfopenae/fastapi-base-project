from abc import ABC, abstractmethod
from .base_entity import BaseEntity
from typing import Iterable

class BaseRepository(ABC):
    
    @abstractmethod
    def commit(self):
        ...
        
    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs) -> None:
        self.commit()
    
    @abstractmethod
    def add(self, other: BaseEntity) -> BaseEntity:
        ...
        
    @abstractmethod
    def list(self) -> Iterable[BaseEntity]:
        ...
    
    @abstractmethod
    def get(self, id: str) -> BaseEntity:
        ...
    
    @abstractmethod
    def update(self, id: str) -> BaseEntity:
        ...
    
    @abstractmethod
    def remove(self, id: str) -> BaseEntity:
        ...