# app/schemas/business_verification.py
import datetime
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any

class BusinessVerificationBase(BaseModel):
    """Base pydantic schema representing shared attributes of BusinessVerification."""
    client_id: int = Field(...)
    status: str = Field(..., max_length=50)
    incorporation_country: str = Field(..., max_length=100)
    registry_url: Optional[str] = Field(None, max_length=500)
    registry_status: Optional[str] = Field(None, max_length=100)
    verified_data_raw: Optional[str] = Field(None)
    verified_at: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)

class BusinessVerificationCreate(BusinessVerificationBase):
    """Schema used during client creation requests for BusinessVerification."""
    pass

class BusinessVerificationUpdate(BaseModel):
    """Schema representing properties that can be updated in BusinessVerification."""
    client_id: Optional[int] = None
    status: Optional[str] = None
    incorporation_country: Optional[str] = None
    registry_url: Optional[str] = None
    registry_status: Optional[str] = None
    verified_data_raw: Optional[str] = None
    verified_at: Optional[datetime.datetime] = None

class BusinessVerificationInDBBase(BusinessVerificationBase):
    id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    metadata_version: int
    is_deleted: bool
    created_by_user: int
    updated_by_user: int

    class Config:
        orm_mode = True

class BusinessVerification(BusinessVerificationInDBBase):
    """API response model wrapper for BusinessVerification."""
    pass

class BusinessVerificationDetailedList(BaseModel):
    items: List[BusinessVerification]
    total_count: int
    page: int
    size: int
    pages_count: int

class BusinessVerificationAuditHistory(BaseModel):
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