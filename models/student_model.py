from pydantic import BaseModel, EmailStr, Field

class Student(BaseModel):
    id: int
    name: str = Field(min_length=2)
    email: EmailStr
    course: str
    semester: int = Field(ge=1, le=8)\
    

class StudentCreate(BaseModel):
    name: str = Field(min_length=2)
    email: EmailStr
    course: str
    semester: int = Field(ge=1, le=8)
