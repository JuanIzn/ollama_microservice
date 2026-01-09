import logging
from fastapi import FastAPI
from app.core.config import settings
from app.api.v1 import chat_router

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

app = FastAPI(title=settings.PROJECT_NAME)

app.include_router(chat_router.router, prefix=settings.API_V1_STR)

@app.on_event("startup")
async def startup_event():
    logger.info(f"Starting {settings.PROJECT_NAME}...")

@app.get("/health")
def health_check():
    logger.debug("Health check requested")
    return {"status": "ok", "service": settings.PROJECT_NAME}