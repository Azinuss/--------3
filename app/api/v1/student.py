from typing import List, Union
from uuid import UUID, uuid4

from fastapi import APIRouter, Depends

from app.api.v1.schemas.student import StudentCreateResponseSchema, StudentCreateRequestSchema, StudentDeleteRequestSchema, StudentDeleteResponseSchema, StudentSchema
from app.core.dependencies.persistance import student_persistence_dependency
from app.domain.student.student import Student
from app.persistence.common import StudentPersistence

router = APIRouter()


@router.post("/create", summary="Create student", description="Create student for students",
             response_model=StudentCreateResponseSchema)
async def create_student(create_request: StudentCreateRequestSchema,
                       student_persistence :StudentPersistence = Depends(student_persistence_dependency)) -> StudentCreateRequestSchema:
    student = student_persistence.save(name=create_request.name, number=create_request.number)
    return StudentCreateResponseSchema(id=student.id)


@router.delete("/delete", summary="Delete student", description="Delete student for students",
             response_model=StudentDeleteResponseSchema)
async def delete_student(delete_request: StudentDeleteRequestSchema,
                       student_persistence :StudentPersistence = Depends(student_persistence_dependency)) -> StudentDeleteRequestSchema:
    student_persistence.delete(name=delete_request.name, number=delete_request.number)
    return StudentDeleteResponseSchema()


@router.get("/", summary="List of students", description= "Get list of students",
            response_model=List[StudentSchema])
async def list_students(student_persistence :StudentPersistence = Depends(student_persistence_dependency)) -> List[StudentSchema]:
    students = student_persistence.list_student()

    return [StudentSchema(id=student.id, name=student.name, number=student.number) for student in students]


@router.get("/{student_id}", summary="Get student", description="Get student by id",
            response_model=Union[StudentSchema,None])
async def get_student(student_id: int,
                    student_persistence :StudentPersistence = Depends(student_persistence_dependency)) -> Union[StudentSchema,None]:
    
    student = student_persistence.get_by_id(student_id)
    if student:
        return StudentSchema(id=student.id, name=student.name, number=student.number)
    else:
        return None