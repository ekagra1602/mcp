from fastapi import FastAPI

from .config import get_settings
from .routers import health, memory

from dotenv import load_dotenv

def create_app() -> FastAPI:
    settings = get_settings()
    app = FastAPI(title=settings.app_name, debug=settings.debug)

    # Include routers
    app.include_router(health.router)
    app.include_router(memory.router)

    return app


app = create_app()

if __name__ == "__main__":
    import uvicorn

    settings = get_settings()
    uvicorn.run(
        "app.main:app",
        host=settings.host,
        port=settings.port,
        reload=settings.debug,
    ) 