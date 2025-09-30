# app/routers/palo_alto.py

from fastapi import APIRouter, HTTPException, Depends
from app.services.service import get_service_status_service
from app.modules.schemas import ServiceStatus

router = APIRouter(
    prefix="/paloalto",
    tags=["Palo Alto Services"]
)

@router.get("/service-status/{service_name}", response_model=ServiceStatus)
async def check_service_status(service_name: str):
    """
    Retrieves the status of a specific service from the Palo Alto firewall.
    """
    try:
        status = get_service_status_service(service_name)
        return status
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {e}")