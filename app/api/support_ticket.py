# app/api/support_ticket.py
from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session
from typing import List, Dict, Any
from app.database import get_db
from app.schemas.support_ticket import SupportTicket, SupportTicketCreate, SupportTicketUpdate, SupportTicketDetailedList
from app.services.support_ticket_service import SupportTicketService

router = APIRouter(prefix='/support_ticket', tags=['SupportTicket'])

@router.get('/', response_model=List[SupportTicket])
def read_support_tickets(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    """
    Retrieve list of SupportTicket objects with optional pagination indexes.
    """
    return SupportTicketService.get_multi(db, skip=skip, limit=limit)

@router.get('/{id}', response_model=SupportTicket)
def read_support_ticket_by_id(id: int, db: Session = Depends(get_db)):
    """
    Retrieve detailed specifications for a specific SupportTicket record.
    """
    return SupportTicketService.get_by_id(db, id=id)

@router.get('/client/{client_id}', response_model=List[SupportTicket])
def read_support_tickets_by_client_id(client_id: int, db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    """
    Retrieve all SupportTicket elements associated with the specified client.
    """
    return SupportTicketService.get_multi_by_client(db, client_id=client_id, skip=skip, limit=limit)

@router.post('/', response_model=SupportTicket, status_code=status.HTTP_201_CREATED)
def create_support_ticket(obj_in: SupportTicketCreate, db: Session = Depends(get_db)):
    """
    Submit and insert a new SupportTicket entity within the system onboarding logs.
    """
    return SupportTicketService.create(db, obj_in=obj_in)

@router.put('/{id}', response_model=SupportTicket)
def update_support_ticket(id: int, obj_in: SupportTicketUpdate, db: Session = Depends(get_db)):
    """
    Modify details of an active SupportTicket configuration object.
    """
    return SupportTicketService.update(db, id=id, obj_in=obj_in)

@router.delete('/{id}', response_model=SupportTicket)
def delete_support_ticket(id: int, db: Session = Depends(get_db)):
    """
    Mark an active SupportTicket object as inactive/deleted.
    """
    return SupportTicketService.delete(db, id=id)

@router.post('/{id}/check-rule-1', response_model=Dict[str, Any])
def trigger_business_checkpoint_1(id: int, db: Session = Depends(get_db)):
    """
    Triggers compliance verification evaluation routine check 1 against SupportTicket.
    """
    return SupportTicketService.business_rule_check_1(db, entity_id=id)

@router.post('/{id}/check-rule-2', response_model=Dict[str, Any])
def trigger_business_checkpoint_2(id: int, db: Session = Depends(get_db)):
    """
    Triggers compliance verification evaluation routine check 2 against SupportTicket.
    """
    return SupportTicketService.business_rule_check_2(db, entity_id=id)

@router.post('/{id}/check-rule-3', response_model=Dict[str, Any])
def trigger_business_checkpoint_3(id: int, db: Session = Depends(get_db)):
    """
    Triggers compliance verification evaluation routine check 3 against SupportTicket.
    """
    return SupportTicketService.business_rule_check_3(db, entity_id=id)

@router.post('/{id}/check-rule-4', response_model=Dict[str, Any])
def trigger_business_checkpoint_4(id: int, db: Session = Depends(get_db)):
    """
    Triggers compliance verification evaluation routine check 4 against SupportTicket.
    """
    return SupportTicketService.business_rule_check_4(db, entity_id=id)

@router.post('/{id}/check-rule-5', response_model=Dict[str, Any])
def trigger_business_checkpoint_5(id: int, db: Session = Depends(get_db)):
    """
    Triggers compliance verification evaluation routine check 5 against SupportTicket.
    """
    return SupportTicketService.business_rule_check_5(db, entity_id=id)

@router.post('/{id}/check-rule-6', response_model=Dict[str, Any])
def trigger_business_checkpoint_6(id: int, db: Session = Depends(get_db)):
    """
    Triggers compliance verification evaluation routine check 6 against SupportTicket.
    """
    return SupportTicketService.business_rule_check_6(db, entity_id=id)

@router.post('/{id}/check-rule-7', response_model=Dict[str, Any])
def trigger_business_checkpoint_7(id: int, db: Session = Depends(get_db)):
    """
    Triggers compliance verification evaluation routine check 7 against SupportTicket.
    """
    return SupportTicketService.business_rule_check_7(db, entity_id=id)

@router.post('/{id}/check-rule-8', response_model=Dict[str, Any])
def trigger_business_checkpoint_8(id: int, db: Session = Depends(get_db)):
    """
    Triggers compliance verification evaluation routine check 8 against SupportTicket.
    """
    return SupportTicketService.business_rule_check_8(db, entity_id=id)

@router.post('/{id}/check-rule-9', response_model=Dict[str, Any])
def trigger_business_checkpoint_9(id: int, db: Session = Depends(get_db)):
    """
    Triggers compliance verification evaluation routine check 9 against SupportTicket.
    """
    return SupportTicketService.business_rule_check_9(db, entity_id=id)

@router.post('/{id}/check-rule-10', response_model=Dict[str, Any])
def trigger_business_checkpoint_10(id: int, db: Session = Depends(get_db)):
    """
    Triggers compliance verification evaluation routine check 10 against SupportTicket.
    """
    return SupportTicketService.business_rule_check_10(db, entity_id=id)

@router.post('/{id}/check-rule-11', response_model=Dict[str, Any])
def trigger_business_checkpoint_11(id: int, db: Session = Depends(get_db)):
    """
    Triggers compliance verification evaluation routine check 11 against SupportTicket.
    """
    return SupportTicketService.business_rule_check_11(db, entity_id=id)

@router.post('/{id}/check-rule-12', response_model=Dict[str, Any])
def trigger_business_checkpoint_12(id: int, db: Session = Depends(get_db)):
    """
    Triggers compliance verification evaluation routine check 12 against SupportTicket.
    """
    return SupportTicketService.business_rule_check_12(db, entity_id=id)

@router.post('/{id}/check-rule-13', response_model=Dict[str, Any])
def trigger_business_checkpoint_13(id: int, db: Session = Depends(get_db)):
    """
    Triggers compliance verification evaluation routine check 13 against SupportTicket.
    """
    return SupportTicketService.business_rule_check_13(db, entity_id=id)

@router.post('/{id}/check-rule-14', response_model=Dict[str, Any])
def trigger_business_checkpoint_14(id: int, db: Session = Depends(get_db)):
    """
    Triggers compliance verification evaluation routine check 14 against SupportTicket.
    """
    return SupportTicketService.business_rule_check_14(db, entity_id=id)

@router.post('/{id}/check-rule-15', response_model=Dict[str, Any])
def trigger_business_checkpoint_15(id: int, db: Session = Depends(get_db)):
    """
    Triggers compliance verification evaluation routine check 15 against SupportTicket.
    """
    return SupportTicketService.business_rule_check_15(db, entity_id=id)

@router.post('/{id}/check-rule-16', response_model=Dict[str, Any])
def trigger_business_checkpoint_16(id: int, db: Session = Depends(get_db)):
    """
    Triggers compliance verification evaluation routine check 16 against SupportTicket.
    """
    return SupportTicketService.business_rule_check_16(db, entity_id=id)

@router.post('/{id}/check-rule-17', response_model=Dict[str, Any])
def trigger_business_checkpoint_17(id: int, db: Session = Depends(get_db)):
    """
    Triggers compliance verification evaluation routine check 17 against SupportTicket.
    """
    return SupportTicketService.business_rule_check_17(db, entity_id=id)

@router.post('/{id}/check-rule-18', response_model=Dict[str, Any])
def trigger_business_checkpoint_18(id: int, db: Session = Depends(get_db)):
    """
    Triggers compliance verification evaluation routine check 18 against SupportTicket.
    """
    return SupportTicketService.business_rule_check_18(db, entity_id=id)

@router.post('/{id}/check-rule-19', response_model=Dict[str, Any])
def trigger_business_checkpoint_19(id: int, db: Session = Depends(get_db)):
    """
    Triggers compliance verification evaluation routine check 19 against SupportTicket.
    """
    return SupportTicketService.business_rule_check_19(db, entity_id=id)

@router.post('/{id}/check-rule-20', response_model=Dict[str, Any])
def trigger_business_checkpoint_20(id: int, db: Session = Depends(get_db)):
    """
    Triggers compliance verification evaluation routine check 20 against SupportTicket.
    """
    return SupportTicketService.business_rule_check_20(db, entity_id=id)

@router.post('/{id}/check-rule-21', response_model=Dict[str, Any])
def trigger_business_checkpoint_21(id: int, db: Session = Depends(get_db)):
    """
    Triggers compliance verification evaluation routine check 21 against SupportTicket.
    """
    return SupportTicketService.business_rule_check_21(db, entity_id=id)

@router.post('/{id}/check-rule-22', response_model=Dict[str, Any])
def trigger_business_checkpoint_22(id: int, db: Session = Depends(get_db)):
    """
    Triggers compliance verification evaluation routine check 22 against SupportTicket.
    """
    return SupportTicketService.business_rule_check_22(db, entity_id=id)

@router.post('/{id}/check-rule-23', response_model=Dict[str, Any])
def trigger_business_checkpoint_23(id: int, db: Session = Depends(get_db)):
    """
    Triggers compliance verification evaluation routine check 23 against SupportTicket.
    """
    return SupportTicketService.business_rule_check_23(db, entity_id=id)

@router.post('/{id}/check-rule-24', response_model=Dict[str, Any])
def trigger_business_checkpoint_24(id: int, db: Session = Depends(get_db)):
    """
    Triggers compliance verification evaluation routine check 24 against SupportTicket.
    """
    return SupportTicketService.business_rule_check_24(db, entity_id=id)

@router.post('/{id}/check-rule-25', response_model=Dict[str, Any])
def trigger_business_checkpoint_25(id: int, db: Session = Depends(get_db)):
    """
    Triggers compliance verification evaluation routine check 25 against SupportTicket.
    """
    return SupportTicketService.business_rule_check_25(db, entity_id=id)
