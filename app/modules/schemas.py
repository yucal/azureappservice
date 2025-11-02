# app/models/schemas.py
from pydantic import BaseModel

class senteceCheckRequest(BaseModel):
    sentence: list[str]
    
    