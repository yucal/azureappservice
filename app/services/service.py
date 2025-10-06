# app/services/palo_alto.py

from app.modules.schemas import ServiceStatus
from app.crud.crud import get_service_status_from_funda


def get_service_status_service(service_name: str) -> ServiceStatus:
    status = get_service_status_from_funda()
    return status