from typing import List, Union
from uuid import UUID, uuid4

from fastapi import APIRouter, Depends

from app.api.v1.schemas.group import GroupCreateResponseSchema, GroupCreateRequestSchema, GroupSchema
from app.core.dependencies.persistance import group_persistence_dependency
from app.domain.group.group import Group
from app.persistence.common import GroupPersistence

router = APIRouter()


@router.post("/", summary="Create group", description="Create group for students",
             response_model=GroupCreateResponseSchema)
async def create_group(create_request: GroupCreateRequestSchema,
                       group_persistence :GroupPersistence = Depends(group_persistence_dependency)) -> GroupCreateRequestSchema:
    group = group_persistence.save(name=create_request.name, number=create_request.number)
    return GroupCreateResponseSchema(id=group.id)


@router.get("/", summary="List of groups", description= "Get list of groups",
            response_model=List[GroupSchema])
async def list_groups(group_persistence :GroupPersistence = Depends(group_persistence_dependency)) -> List[GroupSchema]:
    groups = group_persistence.list_group()

    return [GroupSchema(id=group.id, name=group.name, number=group.number) for group in groups]


@router.get("/{groupe_id}", summary="Get group", description="Get group by id",
            response_model=Union[GroupSchema,None])
async def get_group(group_id: int,
                    group_persistence :GroupPersistence = Depends(group_persistence_dependency)) -> Union[GroupSchema,None]:
    
    group = group_persistence.get_by_id(group_id)
    if group:
        return GroupSchema(id=group.id, name=group.name, number=group.number)
    else:
        return None