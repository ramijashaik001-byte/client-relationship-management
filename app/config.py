# app/config.py
from pydantic import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    PROJECT_NAME: str = "Client Onboarding CRM API"
    API_V1_STR: str = "/api/v1"
    DATABASE_URL: str = "sqlite:///./crm_onboarding.db"
    SECRET_KEY: str = "SUPER_SECRET_SECURITY_PHRASE_FOR_TOKEN_GENERATION_329482038"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    
    # KYC API credentials mock
    KYC_PROVIDER_API_KEY: Optional[str] = "mock_kyc_api_key_123"
    KYC_ENDPOINT: str = "https://api.mockkyc.com/v1"
    
    # Document storage path
    DOCUMENT_STORAGE_DIR: str = "./storage/documents"
    
    class Config:
        case_sensitive = True

settings = Settings()

# API Version 1.0.1 updates
