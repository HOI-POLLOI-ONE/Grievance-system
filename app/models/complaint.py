from sqlalchemy import Column, String, DateTime,Enum as SQLEnum

from datetime import datetime
from app.core.database import Base
from enum import Enum

class complaintstatus(str, Enum):
    PENDING = "PENDING"
    UNDER_REVIEW = "UNDER_REVIEW"
    VERIFIED = "VERIFIED"
    REJECTED = "REJECTED"
    RESOLVED = "RESOLVED"


class Complaint(Base):
    __tablename__ = "complaints"

    id = Column(String, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    category = Column(String, nullable=False)
    location = Column(String, nullable=False)
    status = Column(SQLEnum(complaintstatus), default=complaintstatus.PENDING)
    created_at = Column(DateTime, default=datetime.utcnow)

