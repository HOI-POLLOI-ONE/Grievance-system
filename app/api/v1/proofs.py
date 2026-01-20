from fastapi import APIRouter, UploadFile, File, Form, Depends, HTTPException
from sqlalchemy.orm import Session
import uuid

from app.core.database import get_db
from app.models.proof import Proof
from app.schemas.proof import ProofResponse

router = APIRouter()

@router.post(
    "/complaints/upload-proof",
    response_model=ProofResponse,
    tags=["Proof Upload"]
)
def upload_proof(
    complaint_id: str = Form(...),
    proof: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    allowed_types = ["image/jpeg", "image/png", "application/pdf"]
    if proof.content_type not in allowed_types:
        raise HTTPException(status_code=400, detail="Invalid file type")

    new_proof = Proof(
        id=str(uuid.uuid4()),
        complaint_id=complaint_id,
        filename=proof.filename,
        file_type=proof.content_type
    )

    db.add(new_proof)
    db.commit()
    db.refresh(new_proof)

    return new_proof
