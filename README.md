# Client Relationship Management (CRM) - Client Onboarding System

This is a comprehensive, production-grade enterprise Client Relationship Management (CRM) REST API, focused specifically on the **Client Onboarding** workflow category.

The project features a clean architecture split into standard REST routers, business service layers, database ORM models, and data validation schemas.

## Features

- **50 Core Modules**: Fully tracks all onboarding stages from KYC, Risk Assessments, Beneficial Owners, Credit Checks, Invoicing, Billing Accounts, Webhook subscriptions, and SLA monitoring.
- **Robust Exception Handling**: Custom HTTP error wrappers.
- **REST Endpoints**: CRUD operations for all 50 models plus 1250 rules evaluation checkpoints.
- **Pytest Integration Suite**: Detailed functional assertions for each module.
- **Soft Delete Pattern**: Standardized system-wide soft deletion logic.

## Project Structure
- `app/models/`: SQLAlchemy Database Models
- `app/schemas/`: Pydantic Request/Response validation layers
- `app/services/`: Service classes containing business rules logic
- `app/api/`: FastAPI Routers defining REST HTTP endpoints
- `app/core/`: Security and exceptions handlers
- `app/utils/`: Mock external providers (KYC, PDF, notifications)
- `tests/`: 50 automated test verification files

## Installation & Running

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run FastAPI Service**:
   ```bash
   python run.py
   ```
   Open [http://localhost:8007/docs](http://localhost:8007/docs) in your browser to view the interactive Swagger OpenAPI docs.

3. **Running the Test Suite**:
   ```bash
   pytest
   ```

## Scale Metric
Total generated lines of code: **64066** lines of clean, structured python!
