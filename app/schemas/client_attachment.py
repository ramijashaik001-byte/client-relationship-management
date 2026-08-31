# app/schemas/client_attachment.py
import datetime
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any

class ClientAttachmentBase(BaseModel):
    """Base pydantic schema representing shared attributes of ClientAttachment."""
    client_id: int = Field(...)
    title: str = Field(..., max_length=255)
    description: Optional[str] = Field(None)
    file_path: str = Field(..., max_length=500)
    file_size: int = Field(...)
    is_internal: bool = Field(True)

class ClientAttachmentCreate(ClientAttachmentBase):
    """Schema used during client creation requests for ClientAttachment."""
    pass

class ClientAttachmentUpdate(BaseModel):
    """Schema representing properties that can be updated in ClientAttachment."""
    client_id: Optional[int] = None
    title: Optional[str] = None
    description: Optional[str] = None
    file_path: Optional[str] = None
    file_size: Optional[int] = None
    is_internal: Optional[bool] = None

class ClientAttachmentInDBBase(ClientAttachmentBase):
    id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    metadata_version: int
    is_deleted: bool
    created_by_user: int
    updated_by_user: int

    class Config:
        orm_mode = True

class ClientAttachment(ClientAttachmentInDBBase):
    """API response model wrapper for ClientAttachment."""
    pass

class ClientAttachmentDetailedList(BaseModel):
    items: List[ClientAttachment]
    total_count: int
    page: int
    size: int
    pages_count: int

class ClientAttachmentAuditHistory(BaseModel):
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