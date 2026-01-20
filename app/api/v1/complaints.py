from fastapi import APIRouter,Depends
from app.schemas.complaints import complaint_create,resp_complaint,complaint_stat_update
from datetime import datetime
import uuid
from fastapi import HTTPException

from sqlalchemy.orm import Session
from app.models.complaint import Complaint,complaintstatus
from app.api.deps import get_db



router = APIRouter()

@router.post("/", response_model=resp_complaint)
def create_complaint(complaint:complaint_create,db:Session=Depends(get_db)):
    new_complaint=Complaint(
        id=str(uuid.uuid4()),
        title=complaint.title,
        description=complaint.description,
        category=complaint.category,
        location=complaint.location,
    )
    db.add(new_complaint)
    db.commit()
    db.refresh(new_complaint)
    return {
        "complaint_id": new_complaint.id,
        "title": new_complaint.title,
        "description": new_complaint.description,
        "category": new_complaint.category,
        "location": new_complaint.location,
        "status": new_complaint.status.value,  # Enum -> string
        "created_at": new_complaint.created_at
    }
    
@router.patch("/complaints/{complaint_id}/status", response_model=dict)
def update_complaint_status(
    complaint_id: str,
    status_update:complaint_stat_update, db: Session = Depends(get_db)):
    
    complaint = db.query(Complaint).filter(Complaint.id == complaint_id).first()
    if not complaint:
        raise HTTPException(status_code=404, detail="Complaint not found")
    
    complaint.status = status_update.status
    db.commit()
    db.refresh(complaint)
    return {"complaint_id": complaint.id, "status": complaint.status}
    
    
