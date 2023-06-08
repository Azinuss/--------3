from abc import ABC, abstractmethod
from typing import List
from uuid import UUID

from app.domain.group.group import Group


class GroupPersistence(ABC):
    @abstractmethod
    def save(self, name:str, number:str) -> Group:
        ...

    @abstractmethod
    def get_by_id(self,group_id: int)-> Group:
        ...
        
    @abstractmethod
    def list_group(self)-> List[Group]:
        ...