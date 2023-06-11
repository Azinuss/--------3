from typing import Optional

from sqlmodel import SQLModel, Field

class StudentModel(SQLModel, table=True):
    
    __tablename__ = "student"

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