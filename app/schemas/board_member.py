# app/schemas/board_member.py
import datetime
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any

class BoardMemberBase(BaseModel):
    """Base pydantic schema representing shared attributes of BoardMember."""
    client_id: int = Field(...)
    first_name: str = Field(..., max_length=100)
    last_name: str = Field(..., max_length=100)
    title: str = Field(..., max_length=100)
    date_of_birth: datetime.datetime = Field(...)
    nationality: str = Field(..., max_length=100)
    is_active: bool = Field(True)
    joined_date: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)

class BoardMemberCreate(BoardMemberBase):
    """Schema used during client creation requests for BoardMember."""
    pass

class BoardMemberUpdate(BaseModel):
    """Schema representing properties that can be updated in BoardMember."""
    client_id: Optional[int] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    title: Optional[str] = None
    date_of_birth: Optional[datetime.datetime] = None
    nationality: Optional[str] = None
    is_active: Optional[bool] = None
    joined_date: Optional[datetime.datetime] = None

class BoardMemberInDBBase(BoardMemberBase):
    id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    metadata_version: int
    is_deleted: bool
    created_by_user: int
    updated_by_user: int

    class Config:
        orm_mode = True

class BoardMember(BoardMemberInDBBase):
    """API response model wrapper for BoardMember."""
    pass

class BoardMemberDetailedList(BaseModel):
    items: List[BoardMember]
    total_count: int
    page: int
    size: int
    pages_count: int

class BoardMemberAuditHistory(BaseModel):
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