# app/schemas/document.py
import datetime
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any

class DocumentBase(BaseModel):
    """Base pydantic schema representing shared attributes of Document."""
    client_id: int = Field(...)
    document_type: str = Field(..., max_length=100)
    status: str = Field('PENDING', max_length=50)
    file_path: str = Field(..., max_length=500)
    file_size: int = Field(...)
    mime_type: str = Field(..., max_length=100)
    uploaded_by: int = Field(...)
    verified_by: Optional[int] = Field(None)
    verified_at: Optional[datetime.datetime] = Field(None)
    expires_at: Optional[datetime.datetime] = Field(None)

class DocumentCreate(DocumentBase):
    """Schema used during client creation requests for Document."""
    pass

class DocumentUpdate(BaseModel):
    """Schema representing properties that can be updated in Document."""
    client_id: Optional[int] = None
    document_type: Optional[str] = None
    status: Optional[str] = None
    file_path: Optional[str] = None
    file_size: Optional[int] = None
    mime_type: Optional[str] = None
    uploaded_by: Optional[int] = None
    verified_by: Optional[int] = None
    verified_at: Optional[datetime.datetime] = None
    expires_at: Optional[datetime.datetime] = None

class DocumentInDBBase(DocumentBase):
    id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    metadata_version: int
    is_deleted: bool
    created_by_user: int
    updated_by_user: int

    class Config:
        orm_mode = True

class Document(DocumentInDBBase):
    """API response model wrapper for Document."""
    pass

class DocumentDetailedList(BaseModel):
    items: List[Document]
    total_count: int
    page: int
    size: int
    pages_count: int

class DocumentAuditHistory(BaseModel):
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