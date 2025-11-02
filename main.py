# main.py
from fastapi import FastAPI
from app.routers import router
app_root_path = os.environ.get("FASTAPI_ROOT_PATH", "")
# The `app` instance is what we will import in the Azure Functions entry point.
app = FastAPI(
    title="Sentence API",
    version="1.0.0",
    root_path=app_root_path  # <--- THIS IS THE CRITICAL CHANGE
)

app.include_router(router.router)


@app.get("/")
def read_root():
    return {"message": "Welcome to the Sentence Checker API"}

