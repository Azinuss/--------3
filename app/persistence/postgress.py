from typing import List
from uuid import UUID

from sqlmodel import Session, select

from app.db.models.group import GroupModel
from app.domain.group.group import Group
from app.persistence.common import GroupPersistence

from app.persistence.common import StudentPersistence
from app.domain.student.student import Student
from app.db.models.student import StudentModel

class PostgresGroupPersistence(GroupPersistence):
    def __init__(self,session: Session):
        self.__session = session

    def save(self,name:str, number:str) -> Group:
        group_model = GroupModel(name=name, number=number)
        self.__session.add(group_model)
        self.__session.commit()
        return Group(id=group_model.id, name=group_model.name, number=group_model.number)
    
    def delete(self,name:str, number:str) -> Group:
        query = select(GroupModel).where(GroupModel.name == name and GroupModel.number == number)
        group_model = self.__session.exec(query).first()
        self.__session.delete(group_model)
        self.__session.commit()
        return None

    def get_by_id(self, group_id: int) -> Group:
        query = select(GroupModel).where(GroupModel.id == group_id)
        group_model = self.__session.exec(query).first()
        return Group(id=group_model.id, name=group_model.name, number=group_model.number)

    def list_group(self) -> List[Group]:
        query = select(GroupModel)
        group_models = self.__session.exec(query).all()
        return [Group(id=group_model.id, name=group_model.name, number=group_model.number) for group_model in group_models]
    

class PostgresStudentPersistence(StudentPersistence):
    def __init__(self,session: Session):
        self.__session = session

    def save(self,name:str, number:str) -> Student:
        student_model = StudentModel(name=name, number=number)
        self.__session.add(student_model)
        self.__session.commit()
        return Student(id=student_model.id, name=student_model.name, number=student_model.number)
    
    def delete(self,name:str, number:str) -> Student:
        query = select(StudentModel).where(StudentModel.name == name and StudentModel.number == number)
        student_model = self.__session.exec(query).first()
        self.__session.delete(student_model)
        self.__session.commit()
        return None

    def get_by_id(self, student_id: int) -> Student:
        query = select(StudentModel).where(StudentModel.id == student_id)
        student_model = self.__session.exec(query).first()
        return Student(id=student_model.id, name=student_model.name, number=student_model.number)

    def list_student(self) -> List[Student]:
        query = select(StudentModel)
        student_models = self.__session.exec(query).all()
        return [Group(id=student_model.id, name=student_model.name, number=student_model.number) for student_model in student_models]