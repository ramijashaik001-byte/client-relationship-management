# app/schemas/client_note.py
import datetime
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any

class ClientNoteBase(BaseModel):
    """Base pydantic schema representing shared attributes of ClientNote."""
    client_id: int = Field(...)
    author_id: int = Field(...)
    note_text: str = Field(...)
    is_private: bool = Field(False)

class ClientNoteCreate(ClientNoteBase):
    """Schema used during client creation requests for ClientNote."""
    pass

class ClientNoteUpdate(BaseModel):
    """Schema representing properties that can be updated in ClientNote."""
    client_id: Optional[int] = None
    author_id: Optional[int] = None
    note_text: Optional[str] = None
    is_private: Optional[bool] = None

class ClientNoteInDBBase(ClientNoteBase):
    id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    metadata_version: int
    is_deleted: bool
    created_by_user: int
    updated_by_user: int

    class Config:
        orm_mode = True

class ClientNote(ClientNoteInDBBase):
    """API response model wrapper for ClientNote."""
    pass

class ClientNoteDetailedList(BaseModel):
    items: List[ClientNote]
    total_count: int
    page: int
    size: int
    pages_count: int

class ClientNoteAuditHistory(BaseModel):
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