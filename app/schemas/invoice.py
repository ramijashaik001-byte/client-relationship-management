# app/schemas/invoice.py
import datetime
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any

class InvoiceBase(BaseModel):
    """Base pydantic schema representing shared attributes of Invoice."""
    billing_account_id: int = Field(...)
    invoice_number: str = Field(..., max_length=100)
    status: str = Field('DRAFT', max_length=50)
    issue_date: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)
    due_date: datetime.datetime = Field(...)
    amount_due: float = Field(...)
    amount_paid: float = Field(0.0)
    tax_amount: float = Field(0.0)

class InvoiceCreate(InvoiceBase):
    """Schema used during client creation requests for Invoice."""
    pass

class InvoiceUpdate(BaseModel):
    """Schema representing properties that can be updated in Invoice."""
    billing_account_id: Optional[int] = None
    invoice_number: Optional[str] = None
    status: Optional[str] = None
    issue_date: Optional[datetime.datetime] = None
    due_date: Optional[datetime.datetime] = None
    amount_due: Optional[float] = None
    amount_paid: Optional[float] = None
    tax_amount: Optional[float] = None

class InvoiceInDBBase(InvoiceBase):
    id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    metadata_version: int
    is_deleted: bool
    created_by_user: int
    updated_by_user: int

    class Config:
        orm_mode = True

class Invoice(InvoiceInDBBase):
    """API response model wrapper for Invoice."""
    pass

class InvoiceDetailedList(BaseModel):
    items: List[Invoice]
    total_count: int
    page: int
    size: int
    pages_count: int

class InvoiceAuditHistory(BaseModel):
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