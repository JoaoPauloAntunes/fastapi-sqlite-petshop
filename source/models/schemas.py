from pydantic import BaseModel, Field
from typing import Optional


class PetSchema(BaseModel):
    name: str = Field(...)
    age: int = Field(...)
    avatar: Optional[str] = Field(...)

    class Config:
        schema_extra = {
            "example": {
                # "user_id": 1,
                "name": "Jorjola",
                "age": 25,
                "avatar": "sample",
            }
        }


class UpdatePetSchema(BaseModel):
    name: str = Field(...)
    age: int = Field(...)
    avatar: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "name": "New Name",
                "age": 32,
                "avatar": "sample",
            }
        }


class OutputModel(BaseModel):
    status: int
    data: int

    class Config:
        schema_extra = {
            "example": {
                "status": 201,
                "data": 32,
            }
        }


# Response model from TestDriven
def ResponseModel(data, code):
    return {
        "code": code,
        "data": [data],
        # "message": message,
    }
