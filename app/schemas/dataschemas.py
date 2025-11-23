from pydantic import BaseModel, Field
from typing import Optional

class DataPayload(BaseModel):
    name: str = Field(..., example="John Doe")
    age: int = Field(..., ge=0, example=30)
    email: Optional[str] = Field(None, example="john@example.com")
    is_active: bool = Field(default=True)

    class Config:
        extra = "forbid"
        schema_extra = {
            "example": {
                "name": "John Doe",
                "age": 25,
                "email": "john@example.com",
                "is_active": True,
            }
        }
