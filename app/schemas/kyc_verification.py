# app/schemas/kyc_verification.py
import datetime
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any

class KYCVerificationBase(BaseModel):
    """Base pydantic schema representing shared attributes of KYCVerification."""
    client_id: int = Field(...)
    status: str = Field('IN_PROGRESS', max_length=50)
    screening_type: str = Field(..., max_length=100)
    initiated_by: int = Field(...)
    completed_at: Optional[datetime.datetime] = Field(None)
    risk_rating: Optional[str] = Field(None, max_length=50)
    recommendation: Optional[str] = Field(None, max_length=255)
    compliance_officer_id: Optional[int] = Field(None)

class KYCVerificationCreate(KYCVerificationBase):
    """Schema used during client creation requests for KYCVerification."""
    pass

class KYCVerificationUpdate(BaseModel):
    """Schema representing properties that can be updated in KYCVerification."""
    client_id: Optional[int] = None
    status: Optional[str] = None
    screening_type: Optional[str] = None
    initiated_by: Optional[int] = None
    completed_at: Optional[datetime.datetime] = None
    risk_rating: Optional[str] = None
    recommendation: Optional[str] = None
    compliance_officer_id: Optional[int] = None

class KYCVerificationInDBBase(KYCVerificationBase):
    id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    metadata_version: int
    is_deleted: bool
    created_by_user: int
    updated_by_user: int

    class Config:
        orm_mode = True

class KYCVerification(KYCVerificationInDBBase):
    """API response model wrapper for KYCVerification."""
    pass

class KYCVerificationDetailedList(BaseModel):
    items: List[KYCVerification]
    total_count: int
    page: int
    size: int
    pages_count: int

class KYCVerificationAuditHistory(BaseModel):
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