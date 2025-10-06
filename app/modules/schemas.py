# app/models/schemas.py

from pydantic import BaseModel

class ServiceStatus(BaseModel):
    service_name: str
    status: str
    detail: str