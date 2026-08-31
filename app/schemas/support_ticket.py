# app/schemas/support_ticket.py
import datetime
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any

class SupportTicketBase(BaseModel):
    """Base pydantic schema representing shared attributes of SupportTicket."""
    client_id: int = Field(...)
    reporter_id: int = Field(...)
    title: str = Field(..., max_length=255)
    description: str = Field(...)
    priority: str = Field('MEDIUM', max_length=20)
    status: str = Field('OPEN', max_length=50)
    assigned_team_id: Optional[int] = Field(None)
    resolved_at: Optional[datetime.datetime] = Field(None)

class SupportTicketCreate(SupportTicketBase):
    """Schema used during client creation requests for SupportTicket."""
    pass

class SupportTicketUpdate(BaseModel):
    """Schema representing properties that can be updated in SupportTicket."""
    client_id: Optional[int] = None
    reporter_id: Optional[int] = None
    title: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[str] = None
    status: Optional[str] = None
    assigned_team_id: Optional[int] = None
    resolved_at: Optional[datetime.datetime] = None

class SupportTicketInDBBase(SupportTicketBase):
    id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    metadata_version: int
    is_deleted: bool
    created_by_user: int
    updated_by_user: int

    class Config:
        orm_mode = True

class SupportTicket(SupportTicketInDBBase):
    """API response model wrapper for SupportTicket."""
    pass

class SupportTicketDetailedList(BaseModel):
    items: List[SupportTicket]
    total_count: int
    page: int
    size: int
    pages_count: int

class SupportTicketAuditHistory(BaseModel):
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