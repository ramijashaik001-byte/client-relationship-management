# app/models/contact.py
import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean, Float, Text, Index
from sqlalchemy.orm import relationship
from app.database import Base

class Contact(Base):
    """
    SQLAlchemy DB model for Contact.
    Represents a specific element in the Client Onboarding CRM system.
    """
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey('clients.id'), nullable=False)
    contact_type = Column(String(50), nullable=False)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(255), nullable=False)
    phone = Column(String(50), nullable=True)
    job_title = Column(String(100), nullable=True)
    is_primary_contact = Column(Boolean, default=False, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow, nullable=False)

    # Metadata fields for auditing and tracking changes programmatically
    metadata_version = Column(Integer, default=1, nullable=False)
    is_deleted = Column(Boolean, default=False, nullable=False)
    deleted_at = Column(DateTime, nullable=True)
    created_by_user = Column(Integer, default=1, nullable=False)
    updated_by_user = Column(Integer, default=1, nullable=False)

    def __repr__(self) -> str:
        return f'<Contact(id={self.id})>'

    def validate_entity_state(self) -> bool:
        """
        Evaluates integrity rules for the model entity state before database insertions.
        Returns true if entity is validated and passes basic criteria.
        """
        if self.is_deleted:
            return False
        if not self.contact_type:
            return False
        if not self.first_name:
            return False
        if not self.last_name:
            return False
        if not self.email:
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