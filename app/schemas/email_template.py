# app/schemas/email_template.py
import datetime
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any

class EmailTemplateBase(BaseModel):
    """Base pydantic schema representing shared attributes of EmailTemplate."""
    template_name: str = Field(..., max_length=100)
    subject: str = Field(..., max_length=255)
    body_html: str = Field(...)
    variables_json: Optional[str] = Field(None)

class EmailTemplateCreate(EmailTemplateBase):
    """Schema used during client creation requests for EmailTemplate."""
    pass

class EmailTemplateUpdate(BaseModel):
    """Schema representing properties that can be updated in EmailTemplate."""
    template_name: Optional[str] = None
    subject: Optional[str] = None
    body_html: Optional[str] = None
    variables_json: Optional[str] = None

class EmailTemplateInDBBase(EmailTemplateBase):
    id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    metadata_version: int
    is_deleted: bool
    created_by_user: int
    updated_by_user: int

    class Config:
        orm_mode = True

class EmailTemplate(EmailTemplateInDBBase):
    """API response model wrapper for EmailTemplate."""
    pass

class EmailTemplateDetailedList(BaseModel):
    items: List[EmailTemplate]
    total_count: int
    page: int
    size: int
    pages_count: int

class EmailTemplateAuditHistory(BaseModel):
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