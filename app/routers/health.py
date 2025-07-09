from fastapi import APIRouter

router = APIRouter(prefix="/health", tags=["Health"])


@router.get("/", summary="Health check")
async def health_check() -> dict[str, str]:
    """Simple health check endpoint to verify that the service is running."""
    return {"status": "ok"} 