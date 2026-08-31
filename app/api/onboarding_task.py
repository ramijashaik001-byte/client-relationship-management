# app/api/onboarding_task.py
from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session
from typing import List, Dict, Any
from app.database import get_db
from app.schemas.onboarding_task import OnboardingTask, OnboardingTaskCreate, OnboardingTaskUpdate, OnboardingTaskDetailedList
from app.services.onboarding_task_service import OnboardingTaskService

router = APIRouter(prefix='/onboarding_task', tags=['OnboardingTask'])

@router.get('/', response_model=List[OnboardingTask])
def read_onboarding_tasks(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    """
    Retrieve list of OnboardingTask objects with optional pagination indexes.
    """
    return OnboardingTaskService.get_multi(db, skip=skip, limit=limit)

@router.get('/{id}', response_model=OnboardingTask)
def read_onboarding_task_by_id(id: int, db: Session = Depends(get_db)):
    """
    Retrieve detailed specifications for a specific OnboardingTask record.
    """
    return OnboardingTaskService.get_by_id(db, id=id)

@router.get('/client/{client_id}', response_model=List[OnboardingTask])
def read_onboarding_tasks_by_client_id(client_id: int, db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    """
    Retrieve all OnboardingTask elements associated with the specified client.
    """
    return OnboardingTaskService.get_multi_by_client(db, client_id=client_id, skip=skip, limit=limit)

@router.post('/', response_model=OnboardingTask, status_code=status.HTTP_201_CREATED)
def create_onboarding_task(obj_in: OnboardingTaskCreate, db: Session = Depends(get_db)):
    """
    Submit and insert a new OnboardingTask entity within the system onboarding logs.
    """
    return OnboardingTaskService.create(db, obj_in=obj_in)

@router.put('/{id}', response_model=OnboardingTask)
def update_onboarding_task(id: int, obj_in: OnboardingTaskUpdate, db: Session = Depends(get_db)):
    """
    Modify details of an active OnboardingTask configuration object.
    """
    return OnboardingTaskService.update(db, id=id, obj_in=obj_in)

@router.delete('/{id}', response_model=OnboardingTask)
def delete_onboarding_task(id: int, db: Session = Depends(get_db)):
    """
    Mark an active OnboardingTask object as inactive/deleted.
    """
    return OnboardingTaskService.delete(db, id=id)

@router.post('/{id}/check-rule-1', response_model=Dict[str, Any])
def trigger_business_checkpoint_1(id: int, db: Session = Depends(get_db)):
    """
    Triggers compliance verification evaluation routine check 1 against OnboardingTask.
    """
    return OnboardingTaskService.business_rule_check_1(db, entity_id=id)

@router.post('/{id}/check-rule-2', response_model=Dict[str, Any])
def trigger_business_checkpoint_2(id: int, db: Session = Depends(get_db)):
    """
    Triggers compliance verification evaluation routine check 2 against OnboardingTask.
    """
    return OnboardingTaskService.business_rule_check_2(db, entity_id=id)

@router.post('/{id}/check-rule-3', response_model=Dict[str, Any])
def trigger_business_checkpoint_3(id: int, db: Session = Depends(get_db)):
    """
    Triggers compliance verification evaluation routine check 3 against OnboardingTask.
    """
    return OnboardingTaskService.business_rule_check_3(db, entity_id=id)

@router.post('/{id}/check-rule-4', response_model=Dict[str, Any])
def trigger_business_checkpoint_4(id: int, db: Session = Depends(get_db)):
    """
    Triggers compliance verification evaluation routine check 4 against OnboardingTask.
    """
    return OnboardingTaskService.business_rule_check_4(db, entity_id=id)

@router.post('/{id}/check-rule-5', response_model=Dict[str, Any])
def trigger_business_checkpoint_5(id: int, db: Session = Depends(get_db)):
    """
    Triggers compliance verification evaluation routine check 5 against OnboardingTask.
    """
    return OnboardingTaskService.business_rule_check_5(db, entity_id=id)

@router.post('/{id}/check-rule-6', response_model=Dict[str, Any])
def trigger_business_checkpoint_6(id: int, db: Session = Depends(get_db)):
    """
    Triggers compliance verification evaluation routine check 6 against OnboardingTask.
    """
    return OnboardingTaskService.business_rule_check_6(db, entity_id=id)

@router.post('/{id}/check-rule-7', response_model=Dict[str, Any])
def trigger_business_checkpoint_7(id: int, db: Session = Depends(get_db)):
    """
    Triggers compliance verification evaluation routine check 7 against OnboardingTask.
    """
    return OnboardingTaskService.business_rule_check_7(db, entity_id=id)

@router.post('/{id}/check-rule-8', response_model=Dict[str, Any])
def trigger_business_checkpoint_8(id: int, db: Session = Depends(get_db)):
    """
    Triggers compliance verification evaluation routine check 8 against OnboardingTask.
    """
    return OnboardingTaskService.business_rule_check_8(db, entity_id=id)

@router.post('/{id}/check-rule-9', response_model=Dict[str, Any])
def trigger_business_checkpoint_9(id: int, db: Session = Depends(get_db)):
    """
    Triggers compliance verification evaluation routine check 9 against OnboardingTask.
    """
    return OnboardingTaskService.business_rule_check_9(db, entity_id=id)

@router.post('/{id}/check-rule-10', response_model=Dict[str, Any])
def trigger_business_checkpoint_10(id: int, db: Session = Depends(get_db)):
    """
    Triggers compliance verification evaluation routine check 10 against OnboardingTask.
    """
    return OnboardingTaskService.business_rule_check_10(db, entity_id=id)

@router.post('/{id}/check-rule-11', response_model=Dict[str, Any])
def trigger_business_checkpoint_11(id: int, db: Session = Depends(get_db)):
    """
    Triggers compliance verification evaluation routine check 11 against OnboardingTask.
    """
    return OnboardingTaskService.business_rule_check_11(db, entity_id=id)

@router.post('/{id}/check-rule-12', response_model=Dict[str, Any])
def trigger_business_checkpoint_12(id: int, db: Session = Depends(get_db)):
    """
    Triggers compliance verification evaluation routine check 12 against OnboardingTask.
    """
    return OnboardingTaskService.business_rule_check_12(db, entity_id=id)

@router.post('/{id}/check-rule-13', response_model=Dict[str, Any])
def trigger_business_checkpoint_13(id: int, db: Session = Depends(get_db)):
    """
    Triggers compliance verification evaluation routine check 13 against OnboardingTask.
    """
    return OnboardingTaskService.business_rule_check_13(db, entity_id=id)

@router.post('/{id}/check-rule-14', response_model=Dict[str, Any])
def trigger_business_checkpoint_14(id: int, db: Session = Depends(get_db)):
    """
    Triggers compliance verification evaluation routine check 14 against OnboardingTask.
    """
    return OnboardingTaskService.business_rule_check_14(db, entity_id=id)

@router.post('/{id}/check-rule-15', response_model=Dict[str, Any])
def trigger_business_checkpoint_15(id: int, db: Session = Depends(get_db)):
    """
    Triggers compliance verification evaluation routine check 15 against OnboardingTask.
    """
    return OnboardingTaskService.business_rule_check_15(db, entity_id=id)

@router.post('/{id}/check-rule-16', response_model=Dict[str, Any])
def trigger_business_checkpoint_16(id: int, db: Session = Depends(get_db)):
    """
    Triggers compliance verification evaluation routine check 16 against OnboardingTask.
    """
    return OnboardingTaskService.business_rule_check_16(db, entity_id=id)

@router.post('/{id}/check-rule-17', response_model=Dict[str, Any])
def trigger_business_checkpoint_17(id: int, db: Session = Depends(get_db)):
    """
    Triggers compliance verification evaluation routine check 17 against OnboardingTask.
    """
    return OnboardingTaskService.business_rule_check_17(db, entity_id=id)

@router.post('/{id}/check-rule-18', response_model=Dict[str, Any])
def trigger_business_checkpoint_18(id: int, db: Session = Depends(get_db)):
    """
    Triggers compliance verification evaluation routine check 18 against OnboardingTask.
    """
    return OnboardingTaskService.business_rule_check_18(db, entity_id=id)

@router.post('/{id}/check-rule-19', response_model=Dict[str, Any])
def trigger_business_checkpoint_19(id: int, db: Session = Depends(get_db)):
    """
    Triggers compliance verification evaluation routine check 19 against OnboardingTask.
    """
    return OnboardingTaskService.business_rule_check_19(db, entity_id=id)

@router.post('/{id}/check-rule-20', response_model=Dict[str, Any])
def trigger_business_checkpoint_20(id: int, db: Session = Depends(get_db)):
    """
    Triggers compliance verification evaluation routine check 20 against OnboardingTask.
    """
    return OnboardingTaskService.business_rule_check_20(db, entity_id=id)

@router.post('/{id}/check-rule-21', response_model=Dict[str, Any])
def trigger_business_checkpoint_21(id: int, db: Session = Depends(get_db)):
    """
    Triggers compliance verification evaluation routine check 21 against OnboardingTask.
    """
    return OnboardingTaskService.business_rule_check_21(db, entity_id=id)

@router.post('/{id}/check-rule-22', response_model=Dict[str, Any])
def trigger_business_checkpoint_22(id: int, db: Session = Depends(get_db)):
    """
    Triggers compliance verification evaluation routine check 22 against OnboardingTask.
    """
    return OnboardingTaskService.business_rule_check_22(db, entity_id=id)

@router.post('/{id}/check-rule-23', response_model=Dict[str, Any])
def trigger_business_checkpoint_23(id: int, db: Session = Depends(get_db)):
    """
    Triggers compliance verification evaluation routine check 23 against OnboardingTask.
    """
    return OnboardingTaskService.business_rule_check_23(db, entity_id=id)

@router.post('/{id}/check-rule-24', response_model=Dict[str, Any])
def trigger_business_checkpoint_24(id: int, db: Session = Depends(get_db)):
    """
    Triggers compliance verification evaluation routine check 24 against OnboardingTask.
    """
    return OnboardingTaskService.business_rule_check_24(db, entity_id=id)

@router.post('/{id}/check-rule-25', response_model=Dict[str, Any])
def trigger_business_checkpoint_25(id: int, db: Session = Depends(get_db)):
    """
    Triggers compliance verification evaluation routine check 25 against OnboardingTask.
    """
    return OnboardingTaskService.business_rule_check_25(db, entity_id=id)
