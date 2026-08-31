# app/schemas/product_subscription.py
import datetime
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any

class ProductSubscriptionBase(BaseModel):
    """Base pydantic schema representing shared attributes of ProductSubscription."""
    client_id: int = Field(...)
    product_id: int = Field(...)
    plan_name: str = Field(..., max_length=100)
    status: str = Field('ACTIVE', max_length=50)
    start_date: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)
    renewal_date: Optional[datetime.datetime] = Field(None)
    amount: float = Field(...)
    billing_cycle: str = Field('MONTHLY', max_length=50)

class ProductSubscriptionCreate(ProductSubscriptionBase):
    """Schema used during client creation requests for ProductSubscription."""
    pass

class ProductSubscriptionUpdate(BaseModel):
    """Schema representing properties that can be updated in ProductSubscription."""
    client_id: Optional[int] = None
    product_id: Optional[int] = None
    plan_name: Optional[str] = None
    status: Optional[str] = None
    start_date: Optional[datetime.datetime] = None
    renewal_date: Optional[datetime.datetime] = None
    amount: Optional[float] = None
    billing_cycle: Optional[str] = None

class ProductSubscriptionInDBBase(ProductSubscriptionBase):
    id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    metadata_version: int
    is_deleted: bool
    created_by_user: int
    updated_by_user: int

    class Config:
        orm_mode = True

class ProductSubscription(ProductSubscriptionInDBBase):
    """API response model wrapper for ProductSubscription."""
    pass

class ProductSubscriptionDetailedList(BaseModel):
    items: List[ProductSubscription]
    total_count: int
    page: int
    size: int
    pages_count: int

class ProductSubscriptionAuditHistory(BaseModel):
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