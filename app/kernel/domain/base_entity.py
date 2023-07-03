from dataclasses import dataclass
from abc import ABCMeta
from abc import abstractmethod
from typing import Optional

@dataclass
class BaseEntity(metaclass=ABCMeta):
    id: Optional[str]

    @classmethod
    @abstractmethod
    def from_dict(cls, other: dict):
        ...

    @abstractmethod
    def to_dict(self):
        ...