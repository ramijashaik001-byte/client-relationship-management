# app/schemas/beneficial_owner.py
import datetime
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any

class BeneficialOwnerBase(BaseModel):
    """Base pydantic schema representing shared attributes of BeneficialOwner."""
    client_id: int = Field(...)
    first_name: str = Field(..., max_length=100)
    last_name: str = Field(..., max_length=100)
    date_of_birth: datetime.datetime = Field(...)
    nationality: str = Field(..., max_length=100)
    ownership_percentage: float = Field(...)
    verification_status: str = Field('PENDING', max_length=50)

class BeneficialOwnerCreate(BeneficialOwnerBase):
    """Schema used during client creation requests for BeneficialOwner."""
    pass

class BeneficialOwnerUpdate(BaseModel):
    """Schema representing properties that can be updated in BeneficialOwner."""
    client_id: Optional[int] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    date_of_birth: Optional[datetime.datetime] = None
    nationality: Optional[str] = None
    ownership_percentage: Optional[float] = None
    verification_status: Optional[str] = None

class BeneficialOwnerInDBBase(BeneficialOwnerBase):
    id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    metadata_version: int
    is_deleted: bool
    created_by_user: int
    updated_by_user: int

    class Config:
        orm_mode = True

class BeneficialOwner(BeneficialOwnerInDBBase):
    """API response model wrapper for BeneficialOwner."""
    pass

class BeneficialOwnerDetailedList(BaseModel):
    items: List[BeneficialOwner]
    total_count: int
    page: int
    size: int
    pages_count: int

class BeneficialOwnerAuditHistory(BaseModel):
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