# app/schemas/kyc_check_detail.py
import datetime
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any

class KYCCheckDetailBase(BaseModel):
    """Base pydantic schema representing shared attributes of KYCCheckDetail."""
    kyc_id: int = Field(...)
    check_type: str = Field(..., max_length=100)
    vendor_name: str = Field(..., max_length=100)
    status: str = Field(..., max_length=50)
    result_raw: Optional[str] = Field(None)
    matches_found: bool = Field(False)
    summary: Optional[str] = Field(None, max_length=500)
    executed_at: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)

class KYCCheckDetailCreate(KYCCheckDetailBase):
    """Schema used during client creation requests for KYCCheckDetail."""
    pass

class KYCCheckDetailUpdate(BaseModel):
    """Schema representing properties that can be updated in KYCCheckDetail."""
    kyc_id: Optional[int] = None
    check_type: Optional[str] = None
    vendor_name: Optional[str] = None
    status: Optional[str] = None
    result_raw: Optional[str] = None
    matches_found: Optional[bool] = None
    summary: Optional[str] = None
    executed_at: Optional[datetime.datetime] = None

class KYCCheckDetailInDBBase(KYCCheckDetailBase):
    id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    metadata_version: int
    is_deleted: bool
    created_by_user: int
    updated_by_user: int

    class Config:
        orm_mode = True

class KYCCheckDetail(KYCCheckDetailInDBBase):
    """API response model wrapper for KYCCheckDetail."""
    pass

class KYCCheckDetailDetailedList(BaseModel):
    items: List[KYCCheckDetail]
    total_count: int
    page: int
    size: int
    pages_count: int

class KYCCheckDetailAuditHistory(BaseModel):
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