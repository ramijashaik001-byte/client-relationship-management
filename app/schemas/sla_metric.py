# app/schemas/sla_metric.py
import datetime
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any

class SLAMetricBase(BaseModel):
    """Base pydantic schema representing shared attributes of SLAMetric."""
    entity_name: str = Field(..., max_length=100)
    entity_id: int = Field(...)
    stage_name: str = Field(..., max_length=100)
    start_time: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)
    end_time: Optional[datetime.datetime] = Field(None)
    duration_seconds: Optional[int] = Field(None)
    target_seconds: int = Field(...)
    is_breached: bool = Field(False)

class SLAMetricCreate(SLAMetricBase):
    """Schema used during client creation requests for SLAMetric."""
    pass

class SLAMetricUpdate(BaseModel):
    """Schema representing properties that can be updated in SLAMetric."""
    entity_name: Optional[str] = None
    entity_id: Optional[int] = None
    stage_name: Optional[str] = None
    start_time: Optional[datetime.datetime] = None
    end_time: Optional[datetime.datetime] = None
    duration_seconds: Optional[int] = None
    target_seconds: Optional[int] = None
    is_breached: Optional[bool] = None

class SLAMetricInDBBase(SLAMetricBase):
    id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    metadata_version: int
    is_deleted: bool
    created_by_user: int
    updated_by_user: int

    class Config:
        orm_mode = True

class SLAMetric(SLAMetricInDBBase):
    """API response model wrapper for SLAMetric."""
    pass

class SLAMetricDetailedList(BaseModel):
    items: List[SLAMetric]
    total_count: int
    page: int
    size: int
    pages_count: int

class SLAMetricAuditHistory(BaseModel):
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