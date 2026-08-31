# app/schemas/email_send_log.py
import datetime
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any

class EmailSendLogBase(BaseModel):
    """Base pydantic schema representing shared attributes of EmailSendLog."""
    client_id: int = Field(...)
    template_id: int = Field(...)
    recipient: str = Field(..., max_length=255)
    status: str = Field(..., max_length=50)
    error_message: Optional[str] = Field(None)

class EmailSendLogCreate(EmailSendLogBase):
    """Schema used during client creation requests for EmailSendLog."""
    pass

class EmailSendLogUpdate(BaseModel):
    """Schema representing properties that can be updated in EmailSendLog."""
    client_id: Optional[int] = None
    template_id: Optional[int] = None
    recipient: Optional[str] = None
    status: Optional[str] = None
    error_message: Optional[str] = None

class EmailSendLogInDBBase(EmailSendLogBase):
    id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    metadata_version: int
    is_deleted: bool
    created_by_user: int
    updated_by_user: int

    class Config:
        orm_mode = True

class EmailSendLog(EmailSendLogInDBBase):
    """API response model wrapper for EmailSendLog."""
    pass

class EmailSendLogDetailedList(BaseModel):
    items: List[EmailSendLog]
    total_count: int
    page: int
    size: int
    pages_count: int

class EmailSendLogAuditHistory(BaseModel):
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