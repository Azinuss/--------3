from pydantic import BaseModel


class StudentCreateRequestSchema(BaseModel):
    name: str
    number: str

class StudentCreateResponseSchema(BaseModel):
    id: int

class StudentDeleteRequestSchema(BaseModel):
    name: str
    number: str


class StudentDeleteResponseSchema(BaseModel):
    ...

class StudentSchema(BaseModel):
    id: int
    name: str
    number: str