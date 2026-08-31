# app/schemas/phone_call_log.py
import datetime
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any

class PhoneCallLogBase(BaseModel):
    """Base pydantic schema representing shared attributes of PhoneCallLog."""
    client_id: int = Field(...)
    caller_id: int = Field(...)
    call_direction: str = Field('INBOUND', max_length=10)
    notes: Optional[str] = Field(None)
    call_duration_seconds: int = Field(0)
    scheduled_at: datetime.datetime = Field(...)
    completed_at: Optional[datetime.datetime] = Field(None)

class PhoneCallLogCreate(PhoneCallLogBase):
    """Schema used during client creation requests for PhoneCallLog."""
    pass

class PhoneCallLogUpdate(BaseModel):
    """Schema representing properties that can be updated in PhoneCallLog."""
    client_id: Optional[int] = None
    caller_id: Optional[int] = None
    call_direction: Optional[str] = None
    notes: Optional[str] = None
    call_duration_seconds: Optional[int] = None
    scheduled_at: Optional[datetime.datetime] = None
    completed_at: Optional[datetime.datetime] = None

class PhoneCallLogInDBBase(PhoneCallLogBase):
    id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    metadata_version: int
    is_deleted: bool
    created_by_user: int
    updated_by_user: int

    class Config:
        orm_mode = True

class PhoneCallLog(PhoneCallLogInDBBase):
    """API response model wrapper for PhoneCallLog."""
    pass

class PhoneCallLogDetailedList(BaseModel):
    items: List[PhoneCallLog]
    total_count: int
    page: int
    size: int
    pages_count: int

class PhoneCallLogAuditHistory(BaseModel):
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