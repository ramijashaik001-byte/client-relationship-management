# app/schemas/user_permission.py
import datetime
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any

class UserPermissionBase(BaseModel):
    """Base pydantic schema representing shared attributes of UserPermission."""
    role_name: str = Field(..., max_length=100)
    permission_name: str = Field(..., max_length=100)
    description: Optional[str] = Field(None, max_length=255)
    is_granted: bool = Field(True)

class UserPermissionCreate(UserPermissionBase):
    """Schema used during client creation requests for UserPermission."""
    pass

class UserPermissionUpdate(BaseModel):
    """Schema representing properties that can be updated in UserPermission."""
    role_name: Optional[str] = None
    permission_name: Optional[str] = None
    description: Optional[str] = None
    is_granted: Optional[bool] = None

class UserPermissionInDBBase(UserPermissionBase):
    id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    metadata_version: int
    is_deleted: bool
    created_by_user: int
    updated_by_user: int

    class Config:
        orm_mode = True

class UserPermission(UserPermissionInDBBase):
    """API response model wrapper for UserPermission."""
    pass

class UserPermissionDetailedList(BaseModel):
    items: List[UserPermission]
    total_count: int
    page: int
    size: int
    pages_count: int

class UserPermissionAuditHistory(BaseModel):
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