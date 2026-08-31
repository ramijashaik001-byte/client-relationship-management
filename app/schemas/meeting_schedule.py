# app/schemas/meeting_schedule.py
import datetime
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any

class MeetingScheduleBase(BaseModel):
    """Base pydantic schema representing shared attributes of MeetingSchedule."""
    client_id: int = Field(...)
    host_id: int = Field(...)
    title: str = Field(..., max_length=255)
    description: Optional[str] = Field(None)
    start_time: datetime.datetime = Field(...)
    end_time: datetime.datetime = Field(...)
    meeting_link: Optional[str] = Field(None, max_length=500)
    status: str = Field('SCHEDULED', max_length=50)

class MeetingScheduleCreate(MeetingScheduleBase):
    """Schema used during client creation requests for MeetingSchedule."""
    pass

class MeetingScheduleUpdate(BaseModel):
    """Schema representing properties that can be updated in MeetingSchedule."""
    client_id: Optional[int] = None
    host_id: Optional[int] = None
    title: Optional[str] = None
    description: Optional[str] = None
    start_time: Optional[datetime.datetime] = None
    end_time: Optional[datetime.datetime] = None
    meeting_link: Optional[str] = None
    status: Optional[str] = None

class MeetingScheduleInDBBase(MeetingScheduleBase):
    id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    metadata_version: int
    is_deleted: bool
    created_by_user: int
    updated_by_user: int

    class Config:
        orm_mode = True

class MeetingSchedule(MeetingScheduleInDBBase):
    """API response model wrapper for MeetingSchedule."""
    pass

class MeetingScheduleDetailedList(BaseModel):
    items: List[MeetingSchedule]
    total_count: int
    page: int
    size: int
    pages_count: int

class MeetingScheduleAuditHistory(BaseModel):
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