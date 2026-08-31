# app/schemas/api_key.py
import datetime
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any

class APIKeyBase(BaseModel):
    """Base pydantic schema representing shared attributes of APIKey."""
    name: str = Field(..., max_length=100)
    prefix: str = Field(..., max_length=10)
    hashed_key: str = Field(..., max_length=255)
    client_id: int = Field(...)
    is_active: bool = Field(True)
    expires_at: Optional[datetime.datetime] = Field(None)

class APIKeyCreate(APIKeyBase):
    """Schema used during client creation requests for APIKey."""
    pass

class APIKeyUpdate(BaseModel):
    """Schema representing properties that can be updated in APIKey."""
    name: Optional[str] = None
    prefix: Optional[str] = None
    hashed_key: Optional[str] = None
    client_id: Optional[int] = None
    is_active: Optional[bool] = None
    expires_at: Optional[datetime.datetime] = None

class APIKeyInDBBase(APIKeyBase):
    id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    metadata_version: int
    is_deleted: bool
    created_by_user: int
    updated_by_user: int

    class Config:
        orm_mode = True

class APIKey(APIKeyInDBBase):
    """API response model wrapper for APIKey."""
    pass

class APIKeyDetailedList(BaseModel):
    items: List[APIKey]
    total_count: int
    page: int
    size: int
    pages_count: int

class APIKeyAuditHistory(BaseModel):
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