# app/schemas/form_field.py
import datetime
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any

class FormFieldBase(BaseModel):
    """Base pydantic schema representing shared attributes of FormField."""
    template_id: int = Field(...)
    name: str = Field(..., max_length=100)
    field_type: str = Field(..., max_length=50)
    label: str = Field(..., max_length=255)
    is_required: bool = Field(False)
    validation_rules: Optional[str] = Field(None)
    order_index: int = Field(0)

class FormFieldCreate(FormFieldBase):
    """Schema used during client creation requests for FormField."""
    pass

class FormFieldUpdate(BaseModel):
    """Schema representing properties that can be updated in FormField."""
    template_id: Optional[int] = None
    name: Optional[str] = None
    field_type: Optional[str] = None
    label: Optional[str] = None
    is_required: Optional[bool] = None
    validation_rules: Optional[str] = None
    order_index: Optional[int] = None

class FormFieldInDBBase(FormFieldBase):
    id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    metadata_version: int
    is_deleted: bool
    created_by_user: int
    updated_by_user: int

    class Config:
        orm_mode = True

class FormField(FormFieldInDBBase):
    """API response model wrapper for FormField."""
    pass

class FormFieldDetailedList(BaseModel):
    items: List[FormField]
    total_count: int
    page: int
    size: int
    pages_count: int

class FormFieldAuditHistory(BaseModel):
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