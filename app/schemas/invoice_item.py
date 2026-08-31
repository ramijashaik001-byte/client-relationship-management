# app/schemas/invoice_item.py
import datetime
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any

class InvoiceItemBase(BaseModel):
    """Base pydantic schema representing shared attributes of InvoiceItem."""
    invoice_id: int = Field(...)
    description: str = Field(..., max_length=255)
    quantity: int = Field(1)
    unit_price: float = Field(...)
    tax_rate: float = Field(0.0)
    subtotal: float = Field(...)
    total: float = Field(...)

class InvoiceItemCreate(InvoiceItemBase):
    """Schema used during client creation requests for InvoiceItem."""
    pass

class InvoiceItemUpdate(BaseModel):
    """Schema representing properties that can be updated in InvoiceItem."""
    invoice_id: Optional[int] = None
    description: Optional[str] = None
    quantity: Optional[int] = None
    unit_price: Optional[float] = None
    tax_rate: Optional[float] = None
    subtotal: Optional[float] = None
    total: Optional[float] = None

class InvoiceItemInDBBase(InvoiceItemBase):
    id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    metadata_version: int
    is_deleted: bool
    created_by_user: int
    updated_by_user: int

    class Config:
        orm_mode = True

class InvoiceItem(InvoiceItemInDBBase):
    """API response model wrapper for InvoiceItem."""
    pass

class InvoiceItemDetailedList(BaseModel):
    items: List[InvoiceItem]
    total_count: int
    page: int
    size: int
    pages_count: int

class InvoiceItemAuditHistory(BaseModel):
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