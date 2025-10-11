# main.py
from fastapi import FastAPI
from app.routers import router


# The `app` instance is what we will import in the Azure Functions entry point.
app = FastAPI(
    title="Funda Checker API",
    description="A FastAPI for checking the status of Funda.",
    version="1.0.0",
)

app.include_router(router.router)


@app.get("/")
def read_root():
    return {"message": "Welcome to the Fundo Service Checker API"}

