from pydantic import BaseModel


class GroupCreateRequestSchema(BaseModel):
    name: str
    number: str

class GroupCreateResponseSchema(BaseModel):
    id: int

class GroupDeleteRequestSchema(BaseModel):
    name: str
    number: str

class GroupDeleteResponseSchema(BaseModel):
    ...


class GroupSchema(BaseModel):
    id: int
    name: str
    number: str