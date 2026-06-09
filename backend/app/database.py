from __future__ import annotations

import os
from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker


class Base(DeclarativeBase):
    pass


BASE_DIR = Path(__file__).resolve().parent
default_database_url = f"sqlite:///{(BASE_DIR / 'acceleratorx.db').as_posix()}"
DATABASE_URL = os.getenv("DATABASE_URL", default_database_url)

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
