from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database import get_db
from ..models import Lead
from ..schemas import LeadListItem, LeadRead, StatusUpdate

router = APIRouter(prefix="/api/leads", tags=["leads"])


@router.get("", response_model=list[LeadListItem])
def list_leads(db: Session = Depends(get_db)):
    return db.query(Lead).order_by(Lead.created_at.desc()).all()


@router.get("/{lead_id}", response_model=LeadRead)
def get_lead(lead_id: int, db: Session = Depends(get_db)):
    lead = db.query(Lead).filter(Lead.id == lead_id).first()
    if not lead:
        raise HTTPException(status_code=404, detail="Lead not found")
    return lead


@router.patch("/{lead_id}/status", response_model=LeadRead)
def update_status(lead_id: int, payload: StatusUpdate, db: Session = Depends(get_db)):
    lead = db.query(Lead).filter(Lead.id == lead_id).first()
    if not lead:
        raise HTTPException(status_code=404, detail="Lead not found")
    lead.follow_up_status = payload.status
    db.commit()
    db.refresh(lead)
    return lead
