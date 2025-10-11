# app/crud/palo_alto.py
from typing import Optional
from app.modules.schemas import ServiceStatus
from app.funda.funda import fundabase

def fundabase_instance():
    funda=fundabase()
    return funda.access_funda_api()
def get_service_status_from_funda() -> Optional[ServiceStatus]:
    funda_list=fundabase_instance()
    return ServiceStatus(
        service_name=funda_list,
        status="OK",
        detail="Service is running."
            )