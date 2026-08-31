# app/schemas/webhook_delivery.py
import datetime
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any

class WebhookDeliveryBase(BaseModel):
    """Base pydantic schema representing shared attributes of WebhookDelivery."""
    subscription_id: int = Field(...)
    event_type: str = Field(..., max_length=100)
    status: str = Field(..., max_length=50)
    response_code: Optional[int] = Field(None)
    payload: str = Field(...)
    duration_ms: int = Field(...)

class WebhookDeliveryCreate(WebhookDeliveryBase):
    """Schema used during client creation requests for WebhookDelivery."""
    pass

class WebhookDeliveryUpdate(BaseModel):
    """Schema representing properties that can be updated in WebhookDelivery."""
    subscription_id: Optional[int] = None
    event_type: Optional[str] = None
    status: Optional[str] = None
    response_code: Optional[int] = None
    payload: Optional[str] = None
    duration_ms: Optional[int] = None

class WebhookDeliveryInDBBase(WebhookDeliveryBase):
    id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    metadata_version: int
    is_deleted: bool
    created_by_user: int
    updated_by_user: int

    class Config:
        orm_mode = True

class WebhookDelivery(WebhookDeliveryInDBBase):
    """API response model wrapper for WebhookDelivery."""
    pass

class WebhookDeliveryDetailedList(BaseModel):
    items: List[WebhookDelivery]
    total_count: int
    page: int
    size: int
    pages_count: int

class WebhookDeliveryAuditHistory(BaseModel):
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