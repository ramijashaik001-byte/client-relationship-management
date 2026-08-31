# app/schemas/form_response.py
import datetime
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any

class FormResponseBase(BaseModel):
    """Base pydantic schema representing shared attributes of FormResponse."""
    client_id: int = Field(...)
    template_id: int = Field(...)
    responder_email: str = Field(..., max_length=255)
    answers_json: str = Field(...)
    submitted_at: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)
    score: Optional[int] = Field(None)

class FormResponseCreate(FormResponseBase):
    """Schema used during client creation requests for FormResponse."""
    pass

class FormResponseUpdate(BaseModel):
    """Schema representing properties that can be updated in FormResponse."""
    client_id: Optional[int] = None
    template_id: Optional[int] = None
    responder_email: Optional[str] = None
    answers_json: Optional[str] = None
    submitted_at: Optional[datetime.datetime] = None
    score: Optional[int] = None

class FormResponseInDBBase(FormResponseBase):
    id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    metadata_version: int
    is_deleted: bool
    created_by_user: int
    updated_by_user: int

    class Config:
        orm_mode = True

class FormResponse(FormResponseInDBBase):
    """API response model wrapper for FormResponse."""
    pass

class FormResponseDetailedList(BaseModel):
    items: List[FormResponse]
    total_count: int
    page: int
    size: int
    pages_count: int

class FormResponseAuditHistory(BaseModel):
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