# app/schemas/integration_setup.py
import datetime
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any

class IntegrationSetupBase(BaseModel):
    """Base pydantic schema representing shared attributes of IntegrationSetup."""
    system_name: str = Field(..., max_length=100)
    connection_type: str = Field(..., max_length=50)
    credentials_encrypted: str = Field(...)
    status: str = Field(..., max_length=50)

class IntegrationSetupCreate(IntegrationSetupBase):
    """Schema used during client creation requests for IntegrationSetup."""
    pass

class IntegrationSetupUpdate(BaseModel):
    """Schema representing properties that can be updated in IntegrationSetup."""
    system_name: Optional[str] = None
    connection_type: Optional[str] = None
    credentials_encrypted: Optional[str] = None
    status: Optional[str] = None

class IntegrationSetupInDBBase(IntegrationSetupBase):
    id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    metadata_version: int
    is_deleted: bool
    created_by_user: int
    updated_by_user: int

    class Config:
        orm_mode = True

class IntegrationSetup(IntegrationSetupInDBBase):
    """API response model wrapper for IntegrationSetup."""
    pass

class IntegrationSetupDetailedList(BaseModel):
    items: List[IntegrationSetup]
    total_count: int
    page: int
    size: int
    pages_count: int

class IntegrationSetupAuditHistory(BaseModel):
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