# app/schemas/credit_check.py
import datetime
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any

class CreditCheckBase(BaseModel):
    """Base pydantic schema representing shared attributes of CreditCheck."""
    client_id: int = Field(...)
    score: int = Field(...)
    provider: str = Field(..., max_length=100)
    credit_limit_recommended: float = Field(...)
    status: str = Field(..., max_length=50)
    report_path: Optional[str] = Field(None, max_length=500)
    checked_at: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)
    next_review_date: Optional[datetime.datetime] = Field(None)

class CreditCheckCreate(CreditCheckBase):
    """Schema used during client creation requests for CreditCheck."""
    pass

class CreditCheckUpdate(BaseModel):
    """Schema representing properties that can be updated in CreditCheck."""
    client_id: Optional[int] = None
    score: Optional[int] = None
    provider: Optional[str] = None
    credit_limit_recommended: Optional[float] = None
    status: Optional[str] = None
    report_path: Optional[str] = None
    checked_at: Optional[datetime.datetime] = None
    next_review_date: Optional[datetime.datetime] = None

class CreditCheckInDBBase(CreditCheckBase):
    id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    metadata_version: int
    is_deleted: bool
    created_by_user: int
    updated_by_user: int

    class Config:
        orm_mode = True

class CreditCheck(CreditCheckInDBBase):
    """API response model wrapper for CreditCheck."""
    pass

class CreditCheckDetailedList(BaseModel):
    items: List[CreditCheck]
    total_count: int
    page: int
    size: int
    pages_count: int

class CreditCheckAuditHistory(BaseModel):
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