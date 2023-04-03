from sqlalchemy import create_engine

from app.db.base import Base
import app.config as config

SQLALCHEMY_DATABASE_URL = config.DATABASE_URL

USE_POSTGRESQL = SQLALCHEMY_DATABASE_URL.startswith("postgresql")

if USE_POSTGRESQL:
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
else:
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
    )

Base.metadata.create_all(bind=engine)