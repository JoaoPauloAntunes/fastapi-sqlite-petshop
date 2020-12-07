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
    new_id: int
    status: bool