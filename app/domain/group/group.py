from typing import Union
from uuid import UUID

from pydantic import BaseModel


class Group(BaseModel):
    id: int
    name: str
    number: str

#class GroupStorage:
#    __groups: "list[Group]"
#
#    def __init__(self):
#        self.__groups = []
#
#    def save_group(self, group: Group) -> None:
#        self.__groups.append(group)
#    
#    def list_groups(self) -> "list[Group]":
#        return self.__groups
#    
#    def get_by_id(self,group_id: UUID) -> Union[Group, None]:
#        found_groups = list(filter(lambda gr: gr.id == group_id, self.__groups))
#        if len(found_groups):
#            return found_groups[0]
#        else:
#            return None
#        
#group_storage = GroupStorage()
