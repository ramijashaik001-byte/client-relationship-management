# app/schemas/activity_log.py
import datetime
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any

class ActivityLogBase(BaseModel):
    """Base pydantic schema representing shared attributes of ActivityLog."""
    client_id: int = Field(...)
    user_id: int = Field(...)
    category: str = Field(..., max_length=100)
    description: str = Field(...)
    duration_minutes: int = Field(0)
    activity_date: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)

class ActivityLogCreate(ActivityLogBase):
    """Schema used during client creation requests for ActivityLog."""
    pass

class ActivityLogUpdate(BaseModel):
    """Schema representing properties that can be updated in ActivityLog."""
    client_id: Optional[int] = None
    user_id: Optional[int] = None
    category: Optional[str] = None
    description: Optional[str] = None
    duration_minutes: Optional[int] = None
    activity_date: Optional[datetime.datetime] = None

class ActivityLogInDBBase(ActivityLogBase):
    id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    metadata_version: int
    is_deleted: bool
    created_by_user: int
    updated_by_user: int

    class Config:
        orm_mode = True

class ActivityLog(ActivityLogInDBBase):
    """API response model wrapper for ActivityLog."""
    pass

class ActivityLogDetailedList(BaseModel):
    items: List[ActivityLog]
    total_count: int
    page: int
    size: int
    pages_count: int

class ActivityLogAuditHistory(BaseModel):
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