# app/crud/palo_alto.py
from typing import Optional
from app.modules.schemas import ServiceStatus

def get_service_status_from_panos() -> Optional[ServiceStatus]:
            return ServiceStatus(
                service_name="PAN-OS",
                status="OK",
                detail="Service is running."
            )
        