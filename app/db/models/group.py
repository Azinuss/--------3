from typing import Optional

from sqlmodel import SQLModel, Field

class GroupModel(SQLModel, table=True):
    
    __tablename__ = "group"

    id: Optional[int] = Field(
        primary_key=True,
        default=None
    )

    name:str =Field(
        max_length=100,
        unique=True
    )

    number:str =Field(
        max_length=100,
        unique=True  
    )