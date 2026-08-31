# app/schemas/document_version.py
import datetime
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any

class DocumentVersionBase(BaseModel):
    """Base pydantic schema representing shared attributes of DocumentVersion."""
    document_id: int = Field(...)
    version_number: int = Field(...)
    file_path: str = Field(..., max_length=500)
    file_size: int = Field(...)
    uploaded_by: int = Field(...)
    change_summary: Optional[str] = Field(None, max_length=255)
    hash_checksum: str = Field(..., max_length=64)

class DocumentVersionCreate(DocumentVersionBase):
    """Schema used during client creation requests for DocumentVersion."""
    pass

class DocumentVersionUpdate(BaseModel):
    """Schema representing properties that can be updated in DocumentVersion."""
    document_id: Optional[int] = None
    version_number: Optional[int] = None
    file_path: Optional[str] = None
    file_size: Optional[int] = None
    uploaded_by: Optional[int] = None
    change_summary: Optional[str] = None
    hash_checksum: Optional[str] = None

class DocumentVersionInDBBase(DocumentVersionBase):
    id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    metadata_version: int
    is_deleted: bool
    created_by_user: int
    updated_by_user: int

    class Config:
        orm_mode = True

class DocumentVersion(DocumentVersionInDBBase):
    """API response model wrapper for DocumentVersion."""
    pass

class DocumentVersionDetailedList(BaseModel):
    items: List[DocumentVersion]
    total_count: int
    page: int
    size: int
    pages_count: int

class DocumentVersionAuditHistory(BaseModel):
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