from fastapi import APIRouter, UploadFile, File, Form, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.complaint import Complaint,complaintstatus
from app.models.proof import Proof
import uuid
from datetime import datetime
from app.services.AI_detector import analyze_proof


router = APIRouter(prefix="/complaints", tags=["Proof Upload"])

def run_ai_detection(proof:UploadFile):
    return "FAKE", 0.95

@router.post("/upload-proof")
def upload_proof(
    complaint_id: str = Form(...),
    complaint_category: str = Form(...),
    proof: UploadFile = File(...),
    db: Session = Depends(get_db)):
    
    file_path = f"uploads/{proof.filename}"

    with open(file_path, "wb") as f:
        f.write(proof.file.read())
    
    allowed_types = ["image/jpeg", "image/png", "application/pdf"]
    if proof.content_type not in allowed_types:
        raise HTTPException(status_code=400, detail="Invalid file type")


    complaint = db.query(Complaint).filter(Complaint.id == complaint_id).first()
    if not complaint:
        raise HTTPException(status_code=404, detail="Complaint not found")
    
    if proof.content_type.startswith("image"):
        file_type = "image"
    elif proof.content_type == "application/pdf":
        file_type = "pdf"
    else:
        file_type = "unknown"
        
    ai_result = analyze_proof(proof.filename, complaint.category)

    ai_verdict, ai_confidence = ai_result["verdict"], ai_result["confidence"]

    proof_db = Proof(
        id=str(uuid.uuid4()),
        complaint_id=complaint_id,
        filename=proof.filename,
        file_type=proof.content_type or "unknown", 
        created_at=datetime.utcnow(),
        ai_verdict=ai_verdict,
        ai_confidence=ai_confidence,
        ai_reason = ai_result["reason"],
        content_type=proof.content_type or "unknown"
        )
    
    if ai_verdict == "VALID":
        complaint.status = complaintstatus.UNDER_REVIEW
    else:
        complaint.status = complaintstatus.VERIFIED
        
    if ai_verdict == "INVALID":
        complaint.status = complaintstatus.REJECTED
        
    db.add(proof_db)
    db.commit()

    return {
        "complaint_id": complaint_id,
        "complaint_category": complaint_category,
        "filename": proof.filename,
        "ai_verdict": ai_verdict,
        "ai_confidence": ai_confidence,
        "ai_reason": ai_result["reason"],
        "message": "Proof uploaded successfully"
    }
