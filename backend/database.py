from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

DATABASE_URL = "sqlite+aiosqlite:///sample.db"

engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False, autoflush=False, class_=AsyncSession)

class Base(DeclarativeBase):
    pass

async def get_async_db():
    async with async_session_maker() as session:
        yield session
        