from typing import AsyncGenerator

from sqlalchemy import text
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from core.config import settings


class DatabaseHelper:
    def __init__(
        self,
        url: str = settings.db.url,
        echo: bool = settings.db.echo,
        echo_pool: bool = settings.db.echo_pool,
        pool_size: int = settings.db.pool_size,
        max_overflow: int = settings.db.max_overflow,
    ) -> None:
        self.engine: AsyncEngine = create_async_engine(
            url=url,
            echo=echo,
            echo_pool=echo_pool,
            pool_size=pool_size,
            max_overflow=max_overflow,
        )
        self.session_factory: async_sessionmaker[AsyncSession] = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )

    async def dispose(self) -> None:
        await self.engine.dispose()

    async def session_getter(self) -> AsyncGenerator[AsyncSession, None]:
        async with self.session_factory() as session:
            yield session

    async def test_connection(self):
        try:
            async with self.engine.connect() as conn:
                result = await conn.execute(text("SELECT 1"))
                print("Connection successful, result:", result.scalar())
        except Exception as e:
            print("Connection failed:", e)


db_helper = DatabaseHelper()
