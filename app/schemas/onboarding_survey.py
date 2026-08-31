# app/schemas/onboarding_survey.py
import datetime
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any

class OnboardingSurveyBase(BaseModel):
    """Base pydantic schema representing shared attributes of OnboardingSurvey."""
    survey_name: str = Field(..., max_length=255)
    description: Optional[str] = Field(None)
    welcome_message: Optional[str] = Field(None)
    question_count: int = Field(0)
    is_active: bool = Field(True)

class OnboardingSurveyCreate(OnboardingSurveyBase):
    """Schema used during client creation requests for OnboardingSurvey."""
    pass

class OnboardingSurveyUpdate(BaseModel):
    """Schema representing properties that can be updated in OnboardingSurvey."""
    survey_name: Optional[str] = None
    description: Optional[str] = None
    welcome_message: Optional[str] = None
    question_count: Optional[int] = None
    is_active: Optional[bool] = None

class OnboardingSurveyInDBBase(OnboardingSurveyBase):
    id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    metadata_version: int
    is_deleted: bool
    created_by_user: int
    updated_by_user: int

    class Config:
        orm_mode = True

class OnboardingSurvey(OnboardingSurveyInDBBase):
    """API response model wrapper for OnboardingSurvey."""
    pass

class OnboardingSurveyDetailedList(BaseModel):
    items: List[OnboardingSurvey]
    total_count: int
    page: int
    size: int
    pages_count: int

class OnboardingSurveyAuditHistory(BaseModel):
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