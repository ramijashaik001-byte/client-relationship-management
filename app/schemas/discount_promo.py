# app/schemas/discount_promo.py
import datetime
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any

class DiscountPromoBase(BaseModel):
    """Base pydantic schema representing shared attributes of DiscountPromo."""
    billing_account_id: int = Field(...)
    code: str = Field(..., max_length=50)
    discount_type: str = Field(..., max_length=50)
    value: float = Field(...)
    start_date: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)
    end_date: Optional[datetime.datetime] = Field(None)
    is_active: bool = Field(True)

class DiscountPromoCreate(DiscountPromoBase):
    """Schema used during client creation requests for DiscountPromo."""
    pass

class DiscountPromoUpdate(BaseModel):
    """Schema representing properties that can be updated in DiscountPromo."""
    billing_account_id: Optional[int] = None
    code: Optional[str] = None
    discount_type: Optional[str] = None
    value: Optional[float] = None
    start_date: Optional[datetime.datetime] = None
    end_date: Optional[datetime.datetime] = None
    is_active: Optional[bool] = None

class DiscountPromoInDBBase(DiscountPromoBase):
    id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    metadata_version: int
    is_deleted: bool
    created_by_user: int
    updated_by_user: int

    class Config:
        orm_mode = True

class DiscountPromo(DiscountPromoInDBBase):
    """API response model wrapper for DiscountPromo."""
    pass

class DiscountPromoDetailedList(BaseModel):
    items: List[DiscountPromo]
    total_count: int
    page: int
    size: int
    pages_count: int

class DiscountPromoAuditHistory(BaseModel):
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