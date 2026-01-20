from pydantic import BaseModel
from datetime import datetime
from typing import Optional

from app.models.complaint import complaintstatus

class complaint_create(BaseModel):
    title:str
    description:str
    category:str
    location:str

class resp_complaint(complaint_create):
    complaint_id:str
    status:str
    created_at:datetime
    
class complaint_stat_update(BaseModel):
    status:complaintstatus
