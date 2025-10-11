# app/routers/palo_alto.py

from fastapi import APIRouter, HTTPException
from app.services.service import get_service_status_service
from app.modules.schemas import ServiceStatus

router = APIRouter(
    prefix="/koop",
    tags=["Koop Services"]
)


@router.get("/koop-status", response_model=ServiceStatus)
async def check_service_status():
    """
    Retrieves the status of a specific service from the Palo Alto firewall.
    """
    try:
        status = get_service_status_service()
        return status
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {e}")