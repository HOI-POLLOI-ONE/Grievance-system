
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.router import api_router
from app.core.database import Base, engine
from app.api.v1.auth import router as auth_router
from fastapi import FastAPI
from app.api.v1.proofs import router as proof_router
from app.api.v1.complaints import router as complaint_router

app= FastAPI(
    title="LOKSETU",
    description="a web application where grievances are closed with whole verification n proofs",
    version="1.0.0"
    
)

app.include_router(complaint_router, prefix="/api/v1")
app.include_router(proof_router, prefix="/api/v1")
Base.metadata.create_all(bind=engine)
app.include_router(api_router,prefix="/api/v1")
app.include_router(auth_router,prefix="/api/v1/auth")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")

def root():
    return{
        "message":"the systen is running ",
        "status":"done"
    }





