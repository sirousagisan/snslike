from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite+aiosqlite:///sample.db"
engine = create_engine("sqlite:///todo_app.db")
session_local = sessionmaker(autoflush=False, bind=engine, autocommit=False)

class Base(DeclarativeBase):
    pass


def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()
        