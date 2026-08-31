# app/schemas/compliance_log.py
import datetime
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any

class ComplianceLogBase(BaseModel):
    """Base pydantic schema representing shared attributes of ComplianceLog."""
    client_id: int = Field(...)
    event_type: str = Field(..., max_length=100)
    status: str = Field(..., max_length=50)
    description: str = Field(...)
    compliance_officer_id: int = Field(...)
    notes: Optional[str] = Field(None)

class ComplianceLogCreate(ComplianceLogBase):
    """Schema used during client creation requests for ComplianceLog."""
    pass

class ComplianceLogUpdate(BaseModel):
    """Schema representing properties that can be updated in ComplianceLog."""
    client_id: Optional[int] = None
    event_type: Optional[str] = None
    status: Optional[str] = None
    description: Optional[str] = None
    compliance_officer_id: Optional[int] = None
    notes: Optional[str] = None

class ComplianceLogInDBBase(ComplianceLogBase):
    id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    metadata_version: int
    is_deleted: bool
    created_by_user: int
    updated_by_user: int

    class Config:
        orm_mode = True

class ComplianceLog(ComplianceLogInDBBase):
    """API response model wrapper for ComplianceLog."""
    pass

class ComplianceLogDetailedList(BaseModel):
    items: List[ComplianceLog]
    total_count: int
    page: int
    size: int
    pages_count: int

class ComplianceLogAuditHistory(BaseModel):
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