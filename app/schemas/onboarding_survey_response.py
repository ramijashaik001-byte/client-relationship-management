# app/schemas/onboarding_survey_response.py
import datetime
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any

class OnboardingSurveyResponseBase(BaseModel):
    """Base pydantic schema representing shared attributes of OnboardingSurveyResponse."""
    survey_id: int = Field(...)
    client_id: int = Field(...)
    rating_score: int = Field(..., ge=1, le=10)
    feedback_text: Optional[str] = Field(None)
    submitted_by: str = Field(..., max_length=255)

class OnboardingSurveyResponseCreate(OnboardingSurveyResponseBase):
    """Schema used during client creation requests for OnboardingSurveyResponse."""
    pass

class OnboardingSurveyResponseUpdate(BaseModel):
    """Schema representing properties that can be updated in OnboardingSurveyResponse."""
    survey_id: Optional[int] = None
    client_id: Optional[int] = None
    rating_score: Optional[int] = None
    feedback_text: Optional[str] = None
    submitted_by: Optional[str] = None

class OnboardingSurveyResponseInDBBase(OnboardingSurveyResponseBase):
    id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    metadata_version: int
    is_deleted: bool
    created_by_user: int
    updated_by_user: int

    class Config:
        orm_mode = True

class OnboardingSurveyResponse(OnboardingSurveyResponseInDBBase):
    """API response model wrapper for OnboardingSurveyResponse."""
    pass

class OnboardingSurveyResponseDetailedList(BaseModel):
    items: List[OnboardingSurveyResponse]
    total_count: int
    page: int
    size: int
    pages_count: int

class OnboardingSurveyResponseAuditHistory(BaseModel):
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