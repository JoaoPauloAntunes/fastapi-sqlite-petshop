from pydantic import BaseModel, Field


class CustomerSchema(BaseModel):
    name: str = Field(...)
    age: int = Field(...)
    avatar: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                # "user_id": 1,
                "name": "Jorjola",
                "age": 25,
                "avatar": "/avatar_default",
            }
        }


class putCustomerSchema(BaseModel):
    name: str = Field(...)
    age: int = Field(...)
    avatar: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "name": "New Name",
                "age": 32,
                "avatar": "/avatar_default",
            }
        }