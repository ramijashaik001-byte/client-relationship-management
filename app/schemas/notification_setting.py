# app/schemas/notification_setting.py
import datetime
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any

class NotificationSettingBase(BaseModel):
    """Base pydantic schema representing shared attributes of NotificationSetting."""
    client_id: int = Field(...)
    user_id: int = Field(...)
    notification_type: str = Field(..., max_length=100)
    channel: str = Field('EMAIL', max_length=50)
    is_enabled: bool = Field(True)

class NotificationSettingCreate(NotificationSettingBase):
    """Schema used during client creation requests for NotificationSetting."""
    pass

class NotificationSettingUpdate(BaseModel):
    """Schema representing properties that can be updated in NotificationSetting."""
    client_id: Optional[int] = None
    user_id: Optional[int] = None
    notification_type: Optional[str] = None
    channel: Optional[str] = None
    is_enabled: Optional[bool] = None

class NotificationSettingInDBBase(NotificationSettingBase):
    id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    metadata_version: int
    is_deleted: bool
    created_by_user: int
    updated_by_user: int

    class Config:
        orm_mode = True

class NotificationSetting(NotificationSettingInDBBase):
    """API response model wrapper for NotificationSetting."""
    pass

class NotificationSettingDetailedList(BaseModel):
    items: List[NotificationSetting]
    total_count: int
    page: int
    size: int
    pages_count: int

class NotificationSettingAuditHistory(BaseModel):
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