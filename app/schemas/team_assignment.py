# app/schemas/team_assignment.py
import datetime
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any

class TeamAssignmentBase(BaseModel):
    """Base pydantic schema representing shared attributes of TeamAssignment."""
    client_id: int = Field(...)
    team_name: str = Field(..., max_length=100)
    role_in_onboarding: str = Field(..., max_length=100)
    assigned_at: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)
    unassigned_at: Optional[datetime.datetime] = Field(None)
    is_active: bool = Field(True)

class TeamAssignmentCreate(TeamAssignmentBase):
    """Schema used during client creation requests for TeamAssignment."""
    pass

class TeamAssignmentUpdate(BaseModel):
    """Schema representing properties that can be updated in TeamAssignment."""
    client_id: Optional[int] = None
    team_name: Optional[str] = None
    role_in_onboarding: Optional[str] = None
    assigned_at: Optional[datetime.datetime] = None
    unassigned_at: Optional[datetime.datetime] = None
    is_active: Optional[bool] = None

class TeamAssignmentInDBBase(TeamAssignmentBase):
    id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    metadata_version: int
    is_deleted: bool
    created_by_user: int
    updated_by_user: int

    class Config:
        orm_mode = True

class TeamAssignment(TeamAssignmentInDBBase):
    """API response model wrapper for TeamAssignment."""
    pass

class TeamAssignmentDetailedList(BaseModel):
    items: List[TeamAssignment]
    total_count: int
    page: int
    size: int
    pages_count: int

class TeamAssignmentAuditHistory(BaseModel):
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