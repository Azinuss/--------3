from abc import ABC, abstractmethod
from typing import List

from app.domain.group.group import Group
from app.domain.student.student import Student



class GroupPersistence(ABC):
    @abstractmethod
    def save(self, name:str, number:str) -> Group:
        ...

    @abstractmethod
    def delete(self,name:str, number:str) -> Group:
        ...

    @abstractmethod
    def get_by_id(self,group_id: int)-> Group:
        ...
        
    @abstractmethod
    def list_group(self)-> List[Group]:
        ...

class StudentPersistence(ABC):
    @abstractmethod
    def save(self, name:str, number:str) -> Student:
        ...

    @abstractmethod
    def delete(self,name:str, number:str) -> Student:
        ...

    @abstractmethod
    def get_by_id(self,group_id: int)-> Student:
        ...
        
    @abstractmethod
    def list_student(self)-> List[Student]:
        ...  