# app/schemas/user_role.py
import datetime
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any

class UserRoleBase(BaseModel):
    """Base pydantic schema representing shared attributes of UserRole."""
    user_id: int = Field(...)
    role_name: str = Field(..., max_length=100)
    assigned_by: int = Field(...)

class UserRoleCreate(UserRoleBase):
    """Schema used during client creation requests for UserRole."""
    pass

class UserRoleUpdate(BaseModel):
    """Schema representing properties that can be updated in UserRole."""
    user_id: Optional[int] = None
    role_name: Optional[str] = None
    assigned_by: Optional[int] = None

class UserRoleInDBBase(UserRoleBase):
    id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    metadata_version: int
    is_deleted: bool
    created_by_user: int
    updated_by_user: int

    class Config:
        orm_mode = True

class UserRole(UserRoleInDBBase):
    """API response model wrapper for UserRole."""
    pass

class UserRoleDetailedList(BaseModel):
    items: List[UserRole]
    total_count: int
    page: int
    size: int
    pages_count: int

class UserRoleAuditHistory(BaseModel):
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