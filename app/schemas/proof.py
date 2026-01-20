from pydantic import BaseModel
from datetime import datetime

class ProofResponse(BaseModel):
    id: str
    complaint_id: str
    filename: str
    file_type: str
    created_at: datetime

    class Config:
        from_attributes = True
