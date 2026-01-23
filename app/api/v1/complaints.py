from fastapi import APIRouter,Depends
from app.schemas.complaints import complaint_create,resp_complaint,complaint_stat_update
from datetime import datetime
import uuid
from fastapi import HTTPException

from sqlalchemy.orm import Session
from app.models.complaint import Complaint,complaintstatus
from app.api.deps import get_db
from app.schemas.complaints import complaint_stat_update
from app.api.deps import authority_only
from app.api.deps import get_current_user


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
    
@router.patch("/complaints/{complaint_id}/status")
def update_complaint_status(
    complaint_id: str,
    status_update: complaint_stat_update,
    db: Session = Depends(get_db)
):
    complaint = db.query(Complaint).filter(Complaint.id == complaint_id).first()
    if not complaint:
        raise HTTPException(status_code=404, detail="Complaint not found")

    current_status = complaint.status
    new_status = status_update.status.value

    print("CURRENT DB STATUS:", current_status)
    print("REQUESTED STATUS:", new_status)

    allowed_transitions = {
        complaintstatus.PENDING: [complaintstatus.UNDER_REVIEW],
        complaintstatus.UNDER_REVIEW: [
            complaintstatus.VERIFIED,
            complaintstatus.REJECTED
        ],
        complaintstatus.VERIFIED: [complaintstatus.RESOLVED],
        complaintstatus.RESOLVED: [complaintstatus.CLOSED],
    }

    if current_status not in allowed_transitions:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid current state: {current_status}"
        )

    if new_status not in allowed_transitions[current_status]:
        raise HTTPException(
            status_code=400,
            detail=f"Cannot change status from {current_status} to {new_status}"
        )

    complaint.status = new_status
    db.commit()
    db.refresh(complaint)

    return {
        "message": "Status updated successfully",
        "complaint_id": complaint.id,
        "status": complaint.status
    }

@router.get("/complaints", dependencies=[Depends(authority_only)])
def get_all_complaints(db: Session = Depends(get_db)):
    return db.query(Complaint).all()

@router.get("/my-complaints")
def my_complaints(
    user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return db.query(Complaint).filter(
        Complaint.user_id == user["user_id"]
    ).all()
