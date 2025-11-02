# app/services/palo_alto.py

from app.modules.schemas import senteceCheckRequest
from app.crud import crud


def get_sentence_service() -> senteceCheckRequest:
    status = crud.get_sentences()

    return senteceCheckRequest( sentence=status)
                               