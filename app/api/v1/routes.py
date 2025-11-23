from fastapi import APIRouter
from schemas.dataschemas import DataPayload

router = APIRouter(prefix="/v1", tags=["Data API"])

@router.post("/echo", response_model=DataPayload)
async def echo_data(payload: DataPayload):
    """
    Echo back the received payload.
    """
    return payload
@router.get("/static", response_model=DataPayload)
async def get_static_data():
    """
    Return static predefined data.
    """
    static_data = DataPayload(
        name="Static User",
        age=99,
        email="static@example.com",
        is_active=False
    )
    return static_data