# app/schemas/financial_detail.py
import datetime
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any

class FinancialDetailBase(BaseModel):
    """Base pydantic schema representing shared attributes of FinancialDetail."""
    client_id: int = Field(...)
    fiscal_year: int = Field(...)
    annual_revenue: float = Field(...)
    assets: float = Field(...)
    net_income: float = Field(...)
    currency: str = Field('USD', max_length=3)
    is_audited: bool = Field(False)
    auditor_name: Optional[str] = Field(None, max_length=255)

class FinancialDetailCreate(FinancialDetailBase):
    """Schema used during client creation requests for FinancialDetail."""
    pass

class FinancialDetailUpdate(BaseModel):
    """Schema representing properties that can be updated in FinancialDetail."""
    client_id: Optional[int] = None
    fiscal_year: Optional[int] = None
    annual_revenue: Optional[float] = None
    assets: Optional[float] = None
    net_income: Optional[float] = None
    currency: Optional[str] = None
    is_audited: Optional[bool] = None
    auditor_name: Optional[str] = None

class FinancialDetailInDBBase(FinancialDetailBase):
    id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    metadata_version: int
    is_deleted: bool
    created_by_user: int
    updated_by_user: int

    class Config:
        orm_mode = True

class FinancialDetail(FinancialDetailInDBBase):
    """API response model wrapper for FinancialDetail."""
    pass

class FinancialDetailDetailedList(BaseModel):
    items: List[FinancialDetail]
    total_count: int
    page: int
    size: int
    pages_count: int

class FinancialDetailAuditHistory(BaseModel):
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