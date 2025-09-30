import azure.functions as func
from fastapi import FastAPI
from app.routers.router import router
# You'll need to define your FastAPI app here or import it from a different file.
# For example, import app from your main.py file.
# from ..main import app as fastapi_app

# Or define it directly in this file
fastapi_app = FastAPI()
fastapi_app.include_router(router)
@fastapi_app.get("/hello")
async def hello():
    return {"message": "Hello from FastAPI on Azure Functions!"}

app = func.AsgiFunctionApp(app=fastapi_app, http_auth_level=func.AuthLevel.ANONYMOUS)