from contextlib import asynccontextmanager

import uvicorn
from db.db_helper import db_helper
from fastapi import FastAPI
from loguru import logger

from api import router as api_router
from core.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Startup...")
    await db_helper.test_connection()
    yield
    logger.info("Shutdown...")
    await db_helper.dispose()


main_app = FastAPI(
    lifespan=lifespan,
)

main_app.include_router(api_router)


if __name__ == "__main__":
    uvicorn.run(
        "main:main_app",
        host=settings.run.host,
        port=settings.run.port,
        reload=True,
    )
