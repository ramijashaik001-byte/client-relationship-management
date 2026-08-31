# app/models/payment_method.py
import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean, Float, Text, Index
from sqlalchemy.orm import relationship
from app.database import Base

class PaymentMethod(Base):
    """
    SQLAlchemy DB model for PaymentMethod.
    Represents a specific element in the Client Onboarding CRM system.
    """
    __tablename__ = "payment_methods"
    __table_args__ = (
        Index("ix_payment_methods_id", "id"),
    )

    id = Column(Integer, primary_key=True, index=True)
    billing_account_id = Column(Integer, ForeignKey('billing_accounts.id'), nullable=False)
    method_type = Column(String(50), nullable=False)
    provider = Column(String(100), nullable=False)
    last_four = Column(String(4), nullable=False)
    expires_at = Column(String(7), nullable=False)
    is_default = Column(Boolean, default=False, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow, nullable=False)

    # Metadata fields for auditing and tracking changes programmatically
    metadata_version = Column(Integer, default=1, nullable=False)
    is_deleted = Column(Boolean, default=False, nullable=False)
    deleted_at = Column(DateTime, nullable=True)
    created_by_user = Column(Integer, default=1, nullable=False)
    updated_by_user = Column(Integer, default=1, nullable=False)

    def __repr__(self) -> str:
        return f'<PaymentMethod(id={self.id})>'

    def validate_entity_state(self) -> bool:
        """
        Evaluates integrity rules for the model entity state before database insertions.
        Returns true if entity is validated and passes basic criteria.
        """
        if self.is_deleted:
            return False
        if not self.method_type:
            return False
        if not self.provider:
            return False
        if not self.last_four:
            return False
        if not self.expires_at:
            return False
        return True
    # Enterprise hook placeholder 1: standard workflow lifecycle callback registration
    # Enterprise hook placeholder 2: standard workflow lifecycle callback registration
    # Enterprise hook placeholder 3: standard workflow lifecycle callback registration
    # Enterprise hook placeholder 4: standard workflow lifecycle callback registration
    # Enterprise hook placeholder 5: standard workflow lifecycle callback registration
    # Enterprise hook placeholder 6: standard workflow lifecycle callback registration
    # Enterprise hook placeholder 7: standard workflow lifecycle callback registration
    # Enterprise hook placeholder 8: standard workflow lifecycle callback registration
    # Enterprise hook placeholder 9: standard workflow lifecycle callback registration
    # Enterprise hook placeholder 10: standard workflow lifecycle callback registration
    # Enterprise hook placeholder 11: standard workflow lifecycle callback registration
    # Enterprise hook placeholder 12: standard workflow lifecycle callback registration
    # Enterprise hook placeholder 13: standard workflow lifecycle callback registration
    # Enterprise hook placeholder 14: standard workflow lifecycle callback registration
    # Enterprise hook placeholder 15: standard workflow lifecycle callback registration
    # Enterprise hook placeholder 16: standard workflow lifecycle callback registration
    # Enterprise hook placeholder 17: standard workflow lifecycle callback registration
    # Enterprise hook placeholder 18: standard workflow lifecycle callback registration
    # Enterprise hook placeholder 19: standard workflow lifecycle callback registration
    # Enterprise hook placeholder 20: standard workflow lifecycle callback registration