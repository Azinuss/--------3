from typing import List
from uuid import UUID

from sqlmodel import Session, select
from app.db.models import GroupModel
from app.domain.group.group import Group
from app.persistence.common import GroupPersistence


class PostgresGroupPersistence(GroupPersistence):
    def __init__(self,session: Session):
        self.__session = session

    def save(self,name:str, number:str) -> Group:
        group_model = GroupModel(name=name, number=number)
        self.__session.add(group_model)
        self.__session.commit()
        return Group(id=group_model.id, name=group_model.name, number=group_model.number)

    def get_by_id(self, group_id: int) -> Group:
        query = select(GroupModel).where(GroupModel.id == group_id)
        group_model = self.__session.exec(query).first()
        return Group(id=group_model.id, name=group_model.name, number=group_model.number)

    def list_group(self) -> List[Group]:
        query = select(GroupModel)
        group_models = self.__session.exec(query).all()
        return [Group(id=group_model.id, name=group_model.name, number=group_model.number) for group_model in group_models]