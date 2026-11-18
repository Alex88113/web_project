from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from src.web_project.configs.product_db_config import get_product_settings
from src.web_project.shames.product import ProductBase

DATABASE_URL: str = str(get_product_settings().PRODUCT_DB_DNS)

engine = create_async_engine(DATABASE_URL, echo=True, pool_pre_ping=True)
session_local = async_sessionmaker(engine, expire_on_commit=False)

async def create_table() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(ProductBase.metadata.create_all)

@asynccontextmanager
async def session_scope() -> AsyncGenerator[AsyncSession, None]:
    async with session_local() as session:
        async with session.begin():
            yield session

