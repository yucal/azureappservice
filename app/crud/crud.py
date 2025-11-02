# app/crud/palo_alto.py
from typing import Optional
from app.modules.schemas import senteceCheckRequest
import logging
logging.basicConfig(level=logging.DEBUG)

def get_sentences():
    logging.debug("Fetching sentences from the data source.")
    # Simulate fetching data
    sentence = ["a","b"]
    logging.debug(f"Fetched sentences: {sentence}")
    return sentence