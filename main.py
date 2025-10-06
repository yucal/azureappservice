# main.py
from fastapi import FastAPI
from app.routers.router import router

# Load environment variables from .env file

# The `app` instance is what we will import in the Azure Functions entry point.
app = FastAPI(
    title="Palo Alto Service Checker API",
    description="A FastAPI for checking the status of services on a Palo Alto firewall.",
    version="1.0.0",
)

app.include_router(router)

@app.get("/")

def read_root():
    return {"message": "Welcome to the Palo Alto Service Checker API"}

@app.get("/health")

def health_check():
    return {"status": "BURAK"}
# You can keep the uvicorn run command for local testing outside of Azure
# This part is ignored by Azure Functions but useful for development
