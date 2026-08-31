# app/schemas/integration_log.py
import datetime
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any

class IntegrationLogBase(BaseModel):
    """Base pydantic schema representing shared attributes of IntegrationLog."""
    setup_id: int = Field(...)
    endpoint: str = Field(..., max_length=255)
    direction: str = Field('OUTBOUND', max_length=10)
    status_code: Optional[int] = Field(None)
    payload_preview: Optional[str] = Field(None)
    response_preview: Optional[str] = Field(None)
    duration_ms: int = Field(...)

class IntegrationLogCreate(IntegrationLogBase):
    """Schema used during client creation requests for IntegrationLog."""
    pass

class IntegrationLogUpdate(BaseModel):
    """Schema representing properties that can be updated in IntegrationLog."""
    setup_id: Optional[int] = None
    endpoint: Optional[str] = None
    direction: Optional[str] = None
    status_code: Optional[int] = None
    payload_preview: Optional[str] = None
    response_preview: Optional[str] = None
    duration_ms: Optional[int] = None

class IntegrationLogInDBBase(IntegrationLogBase):
    id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    metadata_version: int
    is_deleted: bool
    created_by_user: int
    updated_by_user: int

    class Config:
        orm_mode = True

class IntegrationLog(IntegrationLogInDBBase):
    """API response model wrapper for IntegrationLog."""
    pass

class IntegrationLogDetailedList(BaseModel):
    items: List[IntegrationLog]
    total_count: int
    page: int
    size: int
    pages_count: int

class IntegrationLogAuditHistory(BaseModel):
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