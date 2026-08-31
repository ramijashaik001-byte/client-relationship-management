# app/schemas/audit_log.py
import datetime
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any

class AuditLogBase(BaseModel):
    """Base pydantic schema representing shared attributes of AuditLog."""
    user_id: int = Field(...)
    client_id: Optional[int] = Field(None)
    action: str = Field(..., max_length=100)
    entity_name: str = Field(..., max_length=100)
    entity_id: int = Field(...)
    before_state: Optional[str] = Field(None)
    after_state: Optional[str] = Field(None)
    ip_address: Optional[str] = Field(None, max_length=50)

class AuditLogCreate(AuditLogBase):
    """Schema used during client creation requests for AuditLog."""
    pass

class AuditLogUpdate(BaseModel):
    """Schema representing properties that can be updated in AuditLog."""
    user_id: Optional[int] = None
    client_id: Optional[int] = None
    action: Optional[str] = None
    entity_name: Optional[str] = None
    entity_id: Optional[int] = None
    before_state: Optional[str] = None
    after_state: Optional[str] = None
    ip_address: Optional[str] = None

class AuditLogInDBBase(AuditLogBase):
    id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    metadata_version: int
    is_deleted: bool
    created_by_user: int
    updated_by_user: int

    class Config:
        orm_mode = True

class AuditLog(AuditLogInDBBase):
    """API response model wrapper for AuditLog."""
    pass

class AuditLogDetailedList(BaseModel):
    items: List[AuditLog]
    total_count: int
    page: int
    size: int
    pages_count: int

class AuditLogAuditHistory(BaseModel):
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