# app/schemas/onboarding_workflow.py
import datetime
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any

class OnboardingWorkflowBase(BaseModel):
    """Base pydantic schema representing shared attributes of OnboardingWorkflow."""
    client_id: int = Field(...)
    workflow_template_id: int = Field(...)
    status: str = Field('IN_PROGRESS', max_length=50)
    assigned_team_id: Optional[int] = Field(None)
    initiated_by: int = Field(...)
    target_completion_date: Optional[datetime.datetime] = Field(None)
    completed_at: Optional[datetime.datetime] = Field(None)

class OnboardingWorkflowCreate(OnboardingWorkflowBase):
    """Schema used during client creation requests for OnboardingWorkflow."""
    pass

class OnboardingWorkflowUpdate(BaseModel):
    """Schema representing properties that can be updated in OnboardingWorkflow."""
    client_id: Optional[int] = None
    workflow_template_id: Optional[int] = None
    status: Optional[str] = None
    assigned_team_id: Optional[int] = None
    initiated_by: Optional[int] = None
    target_completion_date: Optional[datetime.datetime] = None
    completed_at: Optional[datetime.datetime] = None

class OnboardingWorkflowInDBBase(OnboardingWorkflowBase):
    id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    metadata_version: int
    is_deleted: bool
    created_by_user: int
    updated_by_user: int

    class Config:
        orm_mode = True

class OnboardingWorkflow(OnboardingWorkflowInDBBase):
    """API response model wrapper for OnboardingWorkflow."""
    pass

class OnboardingWorkflowDetailedList(BaseModel):
    items: List[OnboardingWorkflow]
    total_count: int
    page: int
    size: int
    pages_count: int

class OnboardingWorkflowAuditHistory(BaseModel):
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