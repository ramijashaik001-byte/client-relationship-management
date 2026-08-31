# app/schemas/risk_assessment.py
import datetime
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any

class RiskAssessmentBase(BaseModel):
    """Base pydantic schema representing shared attributes of RiskAssessment."""
    client_id: int = Field(...)
    screening_score: int = Field(...)
    geography_risk: str = Field(..., max_length=50)
    industry_risk: str = Field(..., max_length=50)
    product_risk: str = Field(..., max_length=50)
    aggregate_risk_score: int = Field(...)
    risk_tier: str = Field(..., max_length=50)
    assessor_notes: Optional[str] = Field(None)
    assessed_at: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)

class RiskAssessmentCreate(RiskAssessmentBase):
    """Schema used during client creation requests for RiskAssessment."""
    pass

class RiskAssessmentUpdate(BaseModel):
    """Schema representing properties that can be updated in RiskAssessment."""
    client_id: Optional[int] = None
    screening_score: Optional[int] = None
    geography_risk: Optional[str] = None
    industry_risk: Optional[str] = None
    product_risk: Optional[str] = None
    aggregate_risk_score: Optional[int] = None
    risk_tier: Optional[str] = None
    assessor_notes: Optional[str] = None
    assessed_at: Optional[datetime.datetime] = None

class RiskAssessmentInDBBase(RiskAssessmentBase):
    id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    metadata_version: int
    is_deleted: bool
    created_by_user: int
    updated_by_user: int

    class Config:
        orm_mode = True

class RiskAssessment(RiskAssessmentInDBBase):
    """API response model wrapper for RiskAssessment."""
    pass

class RiskAssessmentDetailedList(BaseModel):
    items: List[RiskAssessment]
    total_count: int
    page: int
    size: int
    pages_count: int

class RiskAssessmentAuditHistory(BaseModel):
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