from fastapi import FastAPI
from api.v1.routes import router as v1_router

def create_app() -> FastAPI:
    app = FastAPI(
        title="Basic FastAPI Template",
        version="1.0.0",
        description="A maintainable FastAPI project template for senior developers.",
    )

    app.include_router(v1_router)
    return app

app = create_app()
