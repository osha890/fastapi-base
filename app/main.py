from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from core.config import settings
from core.db_helper import db_helper


@asynccontextmanager
async def lifespan(app: FastAPI):
    await db_helper.test_connection()
    yield
    await db_helper.dispose()


main_app = FastAPI(
    lifespan=lifespan,
)


if __name__ == "__main__":
    uvicorn.run(
        "main:main_app",
        host=settings.run.host,
        port=settings.run.port,
        reload=True,
    )
