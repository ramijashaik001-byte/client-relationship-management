# app/schemas/notification_history.py
import datetime
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any

class NotificationHistoryBase(BaseModel):
    """Base pydantic schema representing shared attributes of NotificationHistory."""
    client_id: int = Field(...)
    user_id: int = Field(...)
    channel: str = Field(..., max_length=50)
    subject: str = Field(..., max_length=255)
    body: str = Field(...)
    status: str = Field(..., max_length=50)
    sent_at: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)
    read_at: Optional[datetime.datetime] = Field(None)

class NotificationHistoryCreate(NotificationHistoryBase):
    """Schema used during client creation requests for NotificationHistory."""
    pass

class NotificationHistoryUpdate(BaseModel):
    """Schema representing properties that can be updated in NotificationHistory."""
    client_id: Optional[int] = None
    user_id: Optional[int] = None
    channel: Optional[str] = None
    subject: Optional[str] = None
    body: Optional[str] = None
    status: Optional[str] = None
    sent_at: Optional[datetime.datetime] = None
    read_at: Optional[datetime.datetime] = None

class NotificationHistoryInDBBase(NotificationHistoryBase):
    id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    metadata_version: int
    is_deleted: bool
    created_by_user: int
    updated_by_user: int

    class Config:
        orm_mode = True

class NotificationHistory(NotificationHistoryInDBBase):
    """API response model wrapper for NotificationHistory."""
    pass

class NotificationHistoryDetailedList(BaseModel):
    items: List[NotificationHistory]
    total_count: int
    page: int
    size: int
    pages_count: int

class NotificationHistoryAuditHistory(BaseModel):
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