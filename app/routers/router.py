# app/routers/palo_alto.py

from fastapi import APIRouter, HTTPException
from app.services import service
from app.modules.schemas import senteceCheckRequest

router = APIRouter(
    prefix="/language",
    tags=["Language Services"]
)


@router.get("/sentence",response_model=senteceCheckRequest)
async def get_sentence_router():
    """
    Retrieves the status of a specific service from the Palo Alto firewall.
    """
    try:
        status = service.get_sentence_service()
        return status
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {e}")