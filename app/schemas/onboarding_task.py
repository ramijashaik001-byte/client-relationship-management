# app/schemas/onboarding_task.py
import datetime
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any

class OnboardingTaskBase(BaseModel):
    """Base pydantic schema representing shared attributes of OnboardingTask."""
    workflow_id: int = Field(...)
    name: str = Field(..., max_length=255)
    description: Optional[str] = Field(None)
    status: str = Field('TODO', max_length=50)
    priority: str = Field('MEDIUM', max_length=20)
    assigned_user_id: Optional[int] = Field(None)
    due_date: Optional[datetime.datetime] = Field(None)
    completed_at: Optional[datetime.datetime] = Field(None)
    depends_on_task_id: Optional[int] = Field(None)

class OnboardingTaskCreate(OnboardingTaskBase):
    """Schema used during client creation requests for OnboardingTask."""
    pass

class OnboardingTaskUpdate(BaseModel):
    """Schema representing properties that can be updated in OnboardingTask."""
    workflow_id: Optional[int] = None
    name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
    priority: Optional[str] = None
    assigned_user_id: Optional[int] = None
    due_date: Optional[datetime.datetime] = None
    completed_at: Optional[datetime.datetime] = None
    depends_on_task_id: Optional[int] = None

class OnboardingTaskInDBBase(OnboardingTaskBase):
    id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    metadata_version: int
    is_deleted: bool
    created_by_user: int
    updated_by_user: int

    class Config:
        orm_mode = True

class OnboardingTask(OnboardingTaskInDBBase):
    """API response model wrapper for OnboardingTask."""
    pass

class OnboardingTaskDetailedList(BaseModel):
    items: List[OnboardingTask]
    total_count: int
    page: int
    size: int
    pages_count: int

class OnboardingTaskAuditHistory(BaseModel):
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