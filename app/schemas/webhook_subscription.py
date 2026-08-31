# app/schemas/webhook_subscription.py
import datetime
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any

class WebhookSubscriptionBase(BaseModel):
    """Base pydantic schema representing shared attributes of WebhookSubscription."""
    target_url: str = Field(..., max_length=500)
    events_subscribed: str = Field(..., max_length=255)
    secret_token: str = Field(..., max_length=255)
    is_active: bool = Field(True)

class WebhookSubscriptionCreate(WebhookSubscriptionBase):
    """Schema used during client creation requests for WebhookSubscription."""
    pass

class WebhookSubscriptionUpdate(BaseModel):
    """Schema representing properties that can be updated in WebhookSubscription."""
    target_url: Optional[str] = None
    events_subscribed: Optional[str] = None
    secret_token: Optional[str] = None
    is_active: Optional[bool] = None

class WebhookSubscriptionInDBBase(WebhookSubscriptionBase):
    id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    metadata_version: int
    is_deleted: bool
    created_by_user: int
    updated_by_user: int

    class Config:
        orm_mode = True

class WebhookSubscription(WebhookSubscriptionInDBBase):
    """API response model wrapper for WebhookSubscription."""
    pass

class WebhookSubscriptionDetailedList(BaseModel):
    items: List[WebhookSubscription]
    total_count: int
    page: int
    size: int
    pages_count: int

class WebhookSubscriptionAuditHistory(BaseModel):
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