from sqlalchemy import Column, String, DateTime, ForeignKey , Float
from datetime import datetime
from app.core.database import Base
from sqlalchemy.orm import relationship

class Proof(Base):
    __tablename__ = "proofs"

    id = Column(String, primary_key=True, index=True)
    complaint_id = Column(String, ForeignKey("complaints.id"))
    filename = Column(String, nullable=False)
    file_type = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    ai_verdict = Column(String, nullable=True)
    ai_confidence = Column(Float, nullable=True)
    ai_reason = Column(String, nullable=True)
    content_type = Column(String, nullable=False)
    complaint = relationship("Complaint", back_populates="proof")