from __future__ import annotations

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database import get_db
from ..schemas import AssessmentCreate, LeadRead
from ..services.assessment_service import process_assessment

router = APIRouter(prefix="/api/assessment", tags=["assessment"])


@router.post("/submit", response_model=LeadRead)
def submit_assessment(payload: AssessmentCreate, db: Session = Depends(get_db)):
    # The service handles scoring, recommendation, and counselling note generation.
    return process_assessment(db, payload)
