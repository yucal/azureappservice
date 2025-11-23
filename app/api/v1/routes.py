from fastapi import APIRouter
from schemas.dataschemas import DataPayload
from v1 import data
import logging
router = APIRouter(prefix="/v1", tags=["Data API"])

@router.post("/restaurant", response_model=DataPayload)
async def echo_data(payload: DataPayload):
    """
    Echo back the received payload.
    """
    return payload
@router.get("/restaurant", response_model=DataPayload)
async def get_static_data():
    static_data = data.fetch_restaurant_data()
    logging.info(f"Fetched static restaurant data:{static_data}")
    return static_data