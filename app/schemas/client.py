# app/schemas/client.py
import datetime
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any

class ClientBase(BaseModel):
    """Base pydantic schema representing shared attributes of Client."""
    legal_name: str = Field(..., min_length=2, max_length=255)
    trade_name: Optional[str] = Field(None, max_length=255)
    registration_number: str = Field(..., max_length=100)
    tax_identifier: str = Field(..., max_length=100)
    industry: str = Field(..., max_length=100)
    website: Optional[str] = Field(None, max_length=255)
    size_category: str = Field('MEDIUM', max_length=50)
    onboarding_status: str = Field('PENDING', max_length=50)

class ClientCreate(ClientBase):
    """Schema used during client creation requests for Client."""
    pass

class ClientUpdate(BaseModel):
    """Schema representing properties that can be updated in Client."""
    legal_name: Optional[str] = None
    trade_name: Optional[str] = None
    registration_number: Optional[str] = None
    tax_identifier: Optional[str] = None
    industry: Optional[str] = None
    website: Optional[str] = None
    size_category: Optional[str] = None
    onboarding_status: Optional[str] = None

class ClientInDBBase(ClientBase):
    id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    metadata_version: int
    is_deleted: bool
    created_by_user: int
    updated_by_user: int

    class Config:
        orm_mode = True

class Client(ClientInDBBase):
    """API response model wrapper for Client."""
    pass

class ClientDetailedList(BaseModel):
    items: List[Client]
    total_count: int
    page: int
    size: int
    pages_count: int

class ClientAuditHistory(BaseModel):
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