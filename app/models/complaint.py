from sqlalchemy import Column, String, DateTime,Enum as SQLEnum

from datetime import datetime
from app.core.database import Base
from enum import Enum
from sqlalchemy.orm import relationship

class complaintstatus(str, Enum):
    PENDING = "PENDING"
    VERIFIED = "VERIFIED"
    UNDER_REVIEW = "UNDER_REVIEW"
    REJECTED = "REJECTED"
    RESOLVED = "RESOLVED"
    CLOSED="CLOSED"


class Complaint(Base):
    __tablename__ = "complaints"

    id = Column(String, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    category = Column(String, nullable=False)
    location = Column(String, nullable=False)
    status = Column(String, default=complaintstatus.PENDING)
    created_at = Column(DateTime, default=datetime.utcnow)
    proof=relationship("Proof", back_populates="complaint")
