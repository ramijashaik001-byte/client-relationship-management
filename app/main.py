# app/main.py
import logging
from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.database import engine, Base
from app.core.exceptions import CRMException

from app.api.client import router as client_router
from app.api.address import router as address_router
from app.api.contact import router as contact_router
from app.api.onboarding_workflow import router as onboarding_workflow_router
from app.api.onboarding_task import router as onboarding_task_router
from app.api.document import router as document_router
from app.api.document_version import router as document_version_router
from app.api.document_signature import router as document_signature_router
from app.api.kyc_verification import router as kyc_verification_router
from app.api.kyc_check_detail import router as kyc_check_detail_router
from app.api.credit_check import router as credit_check_router
from app.api.business_verification import router as business_verification_router
from app.api.risk_assessment import router as risk_assessment_router
from app.api.compliance_log import router as compliance_log_router
from app.api.notification_setting import router as notification_setting_router
from app.api.notification_history import router as notification_history_router
from app.api.user_role import router as user_role_router
from app.api.user_permission import router as user_permission_router
from app.api.audit_log import router as audit_log_router
from app.api.client_note import router as client_note_router
from app.api.form_template import router as form_template_router
from app.api.form_field import router as form_field_router
from app.api.form_response import router as form_response_router
from app.api.integration_setup import router as integration_setup_router
from app.api.integration_log import router as integration_log_router
from app.api.api_key import router as api_key_router
from app.api.webhook_subscription import router as webhook_subscription_router
from app.api.webhook_delivery import router as webhook_delivery_router
from app.api.client_attachment import router as client_attachment_router
from app.api.financial_detail import router as financial_detail_router
from app.api.beneficial_owner import router as beneficial_owner_router
from app.api.board_member import router as board_member_router
from app.api.support_ticket import router as support_ticket_router
from app.api.sla_metric import router as sla_metric_router
from app.api.team_assignment import router as team_assignment_router
from app.api.activity_log import router as activity_log_router
from app.api.email_template import router as email_template_router
from app.api.email_send_log import router as email_send_log_router
from app.api.sms_log import router as sms_log_router
from app.api.phone_call_log import router as phone_call_log_router
from app.api.meeting_schedule import router as meeting_schedule_router
from app.api.product_subscription import router as product_subscription_router
from app.api.billing_account import router as billing_account_router
from app.api.billing_address import router as billing_address_router
from app.api.payment_method import router as payment_method_router
from app.api.invoice import router as invoice_router
from app.api.invoice_item import router as invoice_item_router
from app.api.discount_promo import router as discount_promo_router
from app.api.onboarding_survey import router as onboarding_survey_router
from app.api.onboarding_survey_response import router as onboarding_survey_response_router

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger('CRM_App')

# Initialize SQLite database models tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.PROJECT_NAME,
    description='Advanced Enterprise Client Relationship Management System specialized in Automated Client Onboarding workflows, KYC checkpoints compliance, and auditing.',
    version='1.0.0',
    docs_url='/docs',
    redoc_url='/redoc',
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

@app.get('/health', status_code=status.HTTP_200_OK, tags=['System'])
def health_check():
    """
    Standard REST API Health assessment endpoint.
    """
    return {
        'status': 'HEALTHY',
        'database': 'ONLINE',
        'components_loaded': 50,
        'active_workers': 4
    }

@app.exception_handler(CRMException)
def crm_exception_handler(request: Request, exc: CRMException):
    return JSONResponse(
        status_code=exc.status_code,
        content={'detail': exc.detail, 'error_category': 'CRM_BUSINESS_RULE_VIOLATION'}
    )

app.include_router(client_router, prefix=settings.API_V1_STR)
app.include_router(address_router, prefix=settings.API_V1_STR)
app.include_router(contact_router, prefix=settings.API_V1_STR)
app.include_router(onboarding_workflow_router, prefix=settings.API_V1_STR)
app.include_router(onboarding_task_router, prefix=settings.API_V1_STR)
app.include_router(document_router, prefix=settings.API_V1_STR)
app.include_router(document_version_router, prefix=settings.API_V1_STR)
app.include_router(document_signature_router, prefix=settings.API_V1_STR)
app.include_router(kyc_verification_router, prefix=settings.API_V1_STR)
app.include_router(kyc_check_detail_router, prefix=settings.API_V1_STR)
app.include_router(credit_check_router, prefix=settings.API_V1_STR)
app.include_router(business_verification_router, prefix=settings.API_V1_STR)
app.include_router(risk_assessment_router, prefix=settings.API_V1_STR)
app.include_router(compliance_log_router, prefix=settings.API_V1_STR)
app.include_router(notification_setting_router, prefix=settings.API_V1_STR)
app.include_router(notification_history_router, prefix=settings.API_V1_STR)
app.include_router(user_role_router, prefix=settings.API_V1_STR)
app.include_router(user_permission_router, prefix=settings.API_V1_STR)
app.include_router(audit_log_router, prefix=settings.API_V1_STR)
app.include_router(client_note_router, prefix=settings.API_V1_STR)
app.include_router(form_template_router, prefix=settings.API_V1_STR)
app.include_router(form_field_router, prefix=settings.API_V1_STR)
app.include_router(form_response_router, prefix=settings.API_V1_STR)
app.include_router(integration_setup_router, prefix=settings.API_V1_STR)
app.include_router(integration_log_router, prefix=settings.API_V1_STR)
app.include_router(api_key_router, prefix=settings.API_V1_STR)
app.include_router(webhook_subscription_router, prefix=settings.API_V1_STR)
app.include_router(webhook_delivery_router, prefix=settings.API_V1_STR)
app.include_router(client_attachment_router, prefix=settings.API_V1_STR)
app.include_router(financial_detail_router, prefix=settings.API_V1_STR)
app.include_router(beneficial_owner_router, prefix=settings.API_V1_STR)
app.include_router(board_member_router, prefix=settings.API_V1_STR)
app.include_router(support_ticket_router, prefix=settings.API_V1_STR)
app.include_router(sla_metric_router, prefix=settings.API_V1_STR)
app.include_router(team_assignment_router, prefix=settings.API_V1_STR)
app.include_router(activity_log_router, prefix=settings.API_V1_STR)
app.include_router(email_template_router, prefix=settings.API_V1_STR)
app.include_router(email_send_log_router, prefix=settings.API_V1_STR)
app.include_router(sms_log_router, prefix=settings.API_V1_STR)
app.include_router(phone_call_log_router, prefix=settings.API_V1_STR)
app.include_router(meeting_schedule_router, prefix=settings.API_V1_STR)
app.include_router(product_subscription_router, prefix=settings.API_V1_STR)
app.include_router(billing_account_router, prefix=settings.API_V1_STR)
app.include_router(billing_address_router, prefix=settings.API_V1_STR)
app.include_router(payment_method_router, prefix=settings.API_V1_STR)
app.include_router(invoice_router, prefix=settings.API_V1_STR)
app.include_router(invoice_item_router, prefix=settings.API_V1_STR)
app.include_router(discount_promo_router, prefix=settings.API_V1_STR)
app.include_router(onboarding_survey_router, prefix=settings.API_V1_STR)
app.include_router(onboarding_survey_response_router, prefix=settings.API_V1_STR)