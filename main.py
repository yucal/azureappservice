# main.py

from fastapi import FastAPI
from app.routers.router import router

app = FastAPI(
    title="Palo Alto Service Checker API",
    description="A FastAPI for checking the status of services on a Palo Alto firewall.",
    version="1.0.0",
)

# Include the router
app.include_router(router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Palo Alto Service Checker API"}