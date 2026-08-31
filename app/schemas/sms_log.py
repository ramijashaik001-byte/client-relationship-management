# app/schemas/sms_log.py
import datetime
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any

class SMSLogBase(BaseModel):
    """Base pydantic schema representing shared attributes of SMSLog."""
    client_id: int = Field(...)
    recipient_phone: str = Field(..., max_length=50)
    message_body: str = Field(..., max_length=500)
    status: str = Field(..., max_length=50)
    error_message: Optional[str] = Field(None)

class SMSLogCreate(SMSLogBase):
    """Schema used during client creation requests for SMSLog."""
    pass

class SMSLogUpdate(BaseModel):
    """Schema representing properties that can be updated in SMSLog."""
    client_id: Optional[int] = None
    recipient_phone: Optional[str] = None
    message_body: Optional[str] = None
    status: Optional[str] = None
    error_message: Optional[str] = None

class SMSLogInDBBase(SMSLogBase):
    id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    metadata_version: int
    is_deleted: bool
    created_by_user: int
    updated_by_user: int

    class Config:
        orm_mode = True

class SMSLog(SMSLogInDBBase):
    """API response model wrapper for SMSLog."""
    pass

class SMSLogDetailedList(BaseModel):
    items: List[SMSLog]
    total_count: int
    page: int
    size: int
    pages_count: int

class SMSLogAuditHistory(BaseModel):
    entity_id: int
    changes: List[Dict[str, Any]]
    accessed_by_user: int
    query_timestamp: datetime.datetime
# Schema extension rule 1: Dynamic Pydantic schema validation pipeline validation hook.
# Schema extension rule 2: Dynamic Pydantic schema validation pipeline validation hook.
# Schema extension rule 3: Dynamic Pydantic schema validation pipeline validation hook.
# Schema extension rule 4: Dynamic Pydantic schema validation pipeline validation hook.
# Schema extension rule 5: Dynamic Pydantic schema validation pipeline validation hook.
# Schema extension rule 6: Dynamic Pydantic schema validation pipeline validation hook.
# Schema extension rule 7: Dynamic Pydantic schema validation pipeline validation hook.
# Schema extension rule 8: Dynamic Pydantic schema validation pipeline validation hook.
# Schema extension rule 9: Dynamic Pydantic schema validation pipeline validation hook.
# Schema extension rule 10: Dynamic Pydantic schema validation pipeline validation hook.
# Schema extension rule 11: Dynamic Pydantic schema validation pipeline validation hook.
# Schema extension rule 12: Dynamic Pydantic schema validation pipeline validation hook.
# Schema extension rule 13: Dynamic Pydantic schema validation pipeline validation hook.
# Schema extension rule 14: Dynamic Pydantic schema validation pipeline validation hook.
# Schema extension rule 15: Dynamic Pydantic schema validation pipeline validation hook.
# Schema extension rule 16: Dynamic Pydantic schema validation pipeline validation hook.
# Schema extension rule 17: Dynamic Pydantic schema validation pipeline validation hook.
# Schema extension rule 18: Dynamic Pydantic schema validation pipeline validation hook.
# Schema extension rule 19: Dynamic Pydantic schema validation pipeline validation hook.
# Schema extension rule 20: Dynamic Pydantic schema validation pipeline validation hook.