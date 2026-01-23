from app.core.database import SessionLocal

from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer
from jose import jwt
from app.core.jwt import SECRET_KEY, ALGORITHM

security = HTTPBearer()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(token=Depends(security)):
    payload = jwt.decode(token.credentials, SECRET_KEY, algorithms=[ALGORITHM])
    return payload

def authority_only(user=Depends(get_current_user)):
    if user["role"] != "AUTHORITY":
        raise HTTPException(403, "Authority access only")
    return user
