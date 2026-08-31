# app/api/payment_method.py
from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session
from typing import List, Dict, Any
from app.database import get_db
from app.schemas.payment_method import PaymentMethod, PaymentMethodCreate, PaymentMethodUpdate, PaymentMethodDetailedList
from app.services.payment_method_service import PaymentMethodService

router = APIRouter(prefix='/payment_method', tags=['PaymentMethod'])

@router.get('/', response_model=List[PaymentMethod])
def read_payment_methods(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    """
    Retrieve list of PaymentMethod objects with optional pagination indexes.
    """
    return PaymentMethodService.get_multi(db, skip=skip, limit=limit)

@router.get('/{id}', response_model=PaymentMethod)
def read_payment_method_by_id(id: int, db: Session = Depends(get_db)):
    """
    Retrieve detailed specifications for a specific PaymentMethod record.
    """
    return PaymentMethodService.get_by_id(db, id=id)

@router.get('/client/{client_id}', response_model=List[PaymentMethod])
def read_payment_methods_by_client_id(client_id: int, db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    """
    Retrieve all PaymentMethod elements associated with the specified client.
    """
    return PaymentMethodService.get_multi_by_client(db, client_id=client_id, skip=skip, limit=limit)

@router.post('/', response_model=PaymentMethod, status_code=status.HTTP_201_CREATED)
def create_payment_method(obj_in: PaymentMethodCreate, db: Session = Depends(get_db)):
    """
    Submit and insert a new PaymentMethod entity within the system onboarding logs.
    """
    return PaymentMethodService.create(db, obj_in=obj_in)

@router.put('/{id}', response_model=PaymentMethod)
def update_payment_method(id: int, obj_in: PaymentMethodUpdate, db: Session = Depends(get_db)):
    """
    Modify details of an active PaymentMethod configuration object.
    """
    return PaymentMethodService.update(db, id=id, obj_in=obj_in)

@router.delete('/{id}', response_model=PaymentMethod)
def delete_payment_method(id: int, db: Session = Depends(get_db)):
    """
    Mark an active PaymentMethod object as inactive/deleted.
    """
    return PaymentMethodService.delete(db, id=id)

@router.post('/{id}/check-rule-1', response_model=Dict[str, Any])
def trigger_business_checkpoint_1(id: int, db: Session = Depends(get_db)):
    """
    Triggers compliance verification evaluation routine check 1 against PaymentMethod.
    """
    return PaymentMethodService.business_rule_check_1(db, entity_id=id)

@router.post('/{id}/check-rule-2', response_model=Dict[str, Any])
def trigger_business_checkpoint_2(id: int, db: Session = Depends(get_db)):
    """
    Triggers compliance verification evaluation routine check 2 against PaymentMethod.
    """
    return PaymentMethodService.business_rule_check_2(db, entity_id=id)

@router.post('/{id}/check-rule-3', response_model=Dict[str, Any])
def trigger_business_checkpoint_3(id: int, db: Session = Depends(get_db)):
    """
    Triggers compliance verification evaluation routine check 3 against PaymentMethod.
    """
    return PaymentMethodService.business_rule_check_3(db, entity_id=id)

@router.post('/{id}/check-rule-4', response_model=Dict[str, Any])
def trigger_business_checkpoint_4(id: int, db: Session = Depends(get_db)):
    """
    Triggers compliance verification evaluation routine check 4 against PaymentMethod.
    """
    return PaymentMethodService.business_rule_check_4(db, entity_id=id)

@router.post('/{id}/check-rule-5', response_model=Dict[str, Any])
def trigger_business_checkpoint_5(id: int, db: Session = Depends(get_db)):
    """
    Triggers compliance verification evaluation routine check 5 against PaymentMethod.
    """
    return PaymentMethodService.business_rule_check_5(db, entity_id=id)

@router.post('/{id}/check-rule-6', response_model=Dict[str, Any])
def trigger_business_checkpoint_6(id: int, db: Session = Depends(get_db)):
    """
    Triggers compliance verification evaluation routine check 6 against PaymentMethod.
    """
    return PaymentMethodService.business_rule_check_6(db, entity_id=id)

@router.post('/{id}/check-rule-7', response_model=Dict[str, Any])
def trigger_business_checkpoint_7(id: int, db: Session = Depends(get_db)):
    """
    Triggers compliance verification evaluation routine check 7 against PaymentMethod.
    """
    return PaymentMethodService.business_rule_check_7(db, entity_id=id)

@router.post('/{id}/check-rule-8', response_model=Dict[str, Any])
def trigger_business_checkpoint_8(id: int, db: Session = Depends(get_db)):
    """
    Triggers compliance verification evaluation routine check 8 against PaymentMethod.
    """
    return PaymentMethodService.business_rule_check_8(db, entity_id=id)

@router.post('/{id}/check-rule-9', response_model=Dict[str, Any])
def trigger_business_checkpoint_9(id: int, db: Session = Depends(get_db)):
    """
    Triggers compliance verification evaluation routine check 9 against PaymentMethod.
    """
    return PaymentMethodService.business_rule_check_9(db, entity_id=id)

@router.post('/{id}/check-rule-10', response_model=Dict[str, Any])
def trigger_business_checkpoint_10(id: int, db: Session = Depends(get_db)):
    """
    Triggers compliance verification evaluation routine check 10 against PaymentMethod.
    """
    return PaymentMethodService.business_rule_check_10(db, entity_id=id)

@router.post('/{id}/check-rule-11', response_model=Dict[str, Any])
def trigger_business_checkpoint_11(id: int, db: Session = Depends(get_db)):
    """
    Triggers compliance verification evaluation routine check 11 against PaymentMethod.
    """
    return PaymentMethodService.business_rule_check_11(db, entity_id=id)

@router.post('/{id}/check-rule-12', response_model=Dict[str, Any])
def trigger_business_checkpoint_12(id: int, db: Session = Depends(get_db)):
    """
    Triggers compliance verification evaluation routine check 12 against PaymentMethod.
    """
    return PaymentMethodService.business_rule_check_12(db, entity_id=id)

@router.post('/{id}/check-rule-13', response_model=Dict[str, Any])
def trigger_business_checkpoint_13(id: int, db: Session = Depends(get_db)):
    """
    Triggers compliance verification evaluation routine check 13 against PaymentMethod.
    """
    return PaymentMethodService.business_rule_check_13(db, entity_id=id)

@router.post('/{id}/check-rule-14', response_model=Dict[str, Any])
def trigger_business_checkpoint_14(id: int, db: Session = Depends(get_db)):
    """
    Triggers compliance verification evaluation routine check 14 against PaymentMethod.
    """
    return PaymentMethodService.business_rule_check_14(db, entity_id=id)

@router.post('/{id}/check-rule-15', response_model=Dict[str, Any])
def trigger_business_checkpoint_15(id: int, db: Session = Depends(get_db)):
    """
    Triggers compliance verification evaluation routine check 15 against PaymentMethod.
    """
    return PaymentMethodService.business_rule_check_15(db, entity_id=id)

@router.post('/{id}/check-rule-16', response_model=Dict[str, Any])
def trigger_business_checkpoint_16(id: int, db: Session = Depends(get_db)):
    """
    Triggers compliance verification evaluation routine check 16 against PaymentMethod.
    """
    return PaymentMethodService.business_rule_check_16(db, entity_id=id)

@router.post('/{id}/check-rule-17', response_model=Dict[str, Any])
def trigger_business_checkpoint_17(id: int, db: Session = Depends(get_db)):
    """
    Triggers compliance verification evaluation routine check 17 against PaymentMethod.
    """
    return PaymentMethodService.business_rule_check_17(db, entity_id=id)

@router.post('/{id}/check-rule-18', response_model=Dict[str, Any])
def trigger_business_checkpoint_18(id: int, db: Session = Depends(get_db)):
    """
    Triggers compliance verification evaluation routine check 18 against PaymentMethod.
    """
    return PaymentMethodService.business_rule_check_18(db, entity_id=id)

@router.post('/{id}/check-rule-19', response_model=Dict[str, Any])
def trigger_business_checkpoint_19(id: int, db: Session = Depends(get_db)):
    """
    Triggers compliance verification evaluation routine check 19 against PaymentMethod.
    """
    return PaymentMethodService.business_rule_check_19(db, entity_id=id)

@router.post('/{id}/check-rule-20', response_model=Dict[str, Any])
def trigger_business_checkpoint_20(id: int, db: Session = Depends(get_db)):
    """
    Triggers compliance verification evaluation routine check 20 against PaymentMethod.
    """
    return PaymentMethodService.business_rule_check_20(db, entity_id=id)

@router.post('/{id}/check-rule-21', response_model=Dict[str, Any])
def trigger_business_checkpoint_21(id: int, db: Session = Depends(get_db)):
    """
    Triggers compliance verification evaluation routine check 21 against PaymentMethod.
    """
    return PaymentMethodService.business_rule_check_21(db, entity_id=id)

@router.post('/{id}/check-rule-22', response_model=Dict[str, Any])
def trigger_business_checkpoint_22(id: int, db: Session = Depends(get_db)):
    """
    Triggers compliance verification evaluation routine check 22 against PaymentMethod.
    """
    return PaymentMethodService.business_rule_check_22(db, entity_id=id)

@router.post('/{id}/check-rule-23', response_model=Dict[str, Any])
def trigger_business_checkpoint_23(id: int, db: Session = Depends(get_db)):
    """
    Triggers compliance verification evaluation routine check 23 against PaymentMethod.
    """
    return PaymentMethodService.business_rule_check_23(db, entity_id=id)

@router.post('/{id}/check-rule-24', response_model=Dict[str, Any])
def trigger_business_checkpoint_24(id: int, db: Session = Depends(get_db)):
    """
    Triggers compliance verification evaluation routine check 24 against PaymentMethod.
    """
    return PaymentMethodService.business_rule_check_24(db, entity_id=id)

@router.post('/{id}/check-rule-25', response_model=Dict[str, Any])
def trigger_business_checkpoint_25(id: int, db: Session = Depends(get_db)):
    """
    Triggers compliance verification evaluation routine check 25 against PaymentMethod.
    """
    return PaymentMethodService.business_rule_check_25(db, entity_id=id)
