from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.dialects.postgresql import JSONB
from app.db import Base

class TaskResult(Base):
    __tablename__ = 'celery_taskmeta'

    id = Column(Integer, primary_key=True)
    task_id = Column(String, nullable=False, unique=True)
    status = Column(String, nullable=False)
    result = Column(JSONB)