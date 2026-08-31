# app/schemas/payment_method.py
import datetime
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any

class PaymentMethodBase(BaseModel):
    """Base pydantic schema representing shared attributes of PaymentMethod."""
    billing_account_id: int = Field(...)
    method_type: str = Field(..., max_length=50)
    provider: str = Field(..., max_length=100)
    last_four: str = Field(..., max_length=4)
    expires_at: str = Field(..., max_length=7)
    is_default: bool = Field(False)

class PaymentMethodCreate(PaymentMethodBase):
    """Schema used during client creation requests for PaymentMethod."""
    pass

class PaymentMethodUpdate(BaseModel):
    """Schema representing properties that can be updated in PaymentMethod."""
    billing_account_id: Optional[int] = None
    method_type: Optional[str] = None
    provider: Optional[str] = None
    last_four: Optional[str] = None
    expires_at: Optional[str] = None
    is_default: Optional[bool] = None

class PaymentMethodInDBBase(PaymentMethodBase):
    id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    metadata_version: int
    is_deleted: bool
    created_by_user: int
    updated_by_user: int

    class Config:
        orm_mode = True

class PaymentMethod(PaymentMethodInDBBase):
    """API response model wrapper for PaymentMethod."""
    pass

class PaymentMethodDetailedList(BaseModel):
    items: List[PaymentMethod]
    total_count: int
    page: int
    size: int
    pages_count: int

class PaymentMethodAuditHistory(BaseModel):
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