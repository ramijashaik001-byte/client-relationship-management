# app/schemas/billing_account.py
import datetime
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any

class BillingAccountBase(BaseModel):
    """Base pydantic schema representing shared attributes of BillingAccount."""
    client_id: int = Field(...)
    account_number: str = Field(..., max_length=100)
    currency: str = Field('USD', max_length=3)
    status: str = Field('ACTIVE', max_length=50)
    payment_terms_days: int = Field(30)
    tax_exemption_code: Optional[str] = Field(None, max_length=100)

class BillingAccountCreate(BillingAccountBase):
    """Schema used during client creation requests for BillingAccount."""
    pass

class BillingAccountUpdate(BaseModel):
    """Schema representing properties that can be updated in BillingAccount."""
    client_id: Optional[int] = None
    account_number: Optional[str] = None
    currency: Optional[str] = None
    status: Optional[str] = None
    payment_terms_days: Optional[int] = None
    tax_exemption_code: Optional[str] = None

class BillingAccountInDBBase(BillingAccountBase):
    id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    metadata_version: int
    is_deleted: bool
    created_by_user: int
    updated_by_user: int

    class Config:
        orm_mode = True

class BillingAccount(BillingAccountInDBBase):
    """API response model wrapper for BillingAccount."""
    pass

class BillingAccountDetailedList(BaseModel):
    items: List[BillingAccount]
    total_count: int
    page: int
    size: int
    pages_count: int

class BillingAccountAuditHistory(BaseModel):
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