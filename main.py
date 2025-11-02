# main.py
from fastapi import FastAPI
from app.routers import router

app = FastAPI(
    title="Sentence API",
    version="1.0.0",
)

app.include_router(router.router)


@app.get("/")
def read_root():
    return {"message": "Welcome to the Sentence Checker API"}

