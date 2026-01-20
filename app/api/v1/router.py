from fastapi import APIRouter
from app.api.v1 import complaints, proofs

api_router = APIRouter()

api_router.include_router(complaints.router, tags=["Complaints"])
api_router.include_router(proofs.router, tags=["Proof Upload"])
