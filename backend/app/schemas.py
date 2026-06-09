from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import BaseModel, EmailStr, Field


FollowUpStatus = Literal["New", "Contacted", "Call Booked", "Enrolled", "Not Interested"]


class AssessmentCreate(BaseModel):
    user_type: str = Field(min_length=1)
    current_role: str = Field(min_length=1)
    education_background: str = Field(min_length=1)
    ai_skill_level: str = Field(min_length=1)
    goal: str = Field(min_length=1)
    timeline: str = Field(min_length=1)
    budget_readiness: str = Field(min_length=1)
    weekly_availability: str = Field(min_length=1)
    preferred_learning_mode: str = Field(min_length=1)
    contact_name: str = Field(min_length=1)
    contact_email: EmailStr
    contact_phone: str = Field(min_length=5)


class LeadRead(BaseModel):
    id: int
    created_at: datetime
    updated_at: datetime
    user_type: str
    current_role: str
    education_background: str
    ai_skill_level: str
    goal: str
    timeline: str
    budget_readiness: str
    weekly_availability: str
    preferred_learning_mode: str
    contact_name: str
    contact_email: str
    contact_phone: str
    recommended_program: str
    recommendation_reason: str
    readiness_level: str
    skill_gap_summary: str
    next_step: str
    lead_score: int
    category: str
    follow_up_status: str
    counsellor_notes: str
    next_action: str
    answers_json: str
    score_breakdown: str

    model_config = {"from_attributes": True}


class LeadListItem(BaseModel):
    id: int
    created_at: datetime
    contact_name: str
    contact_email: str
    contact_phone: str
    user_type: str
    goal: str
    recommended_program: str
    lead_score: int
    category: str
    timeline: str
    budget_readiness: str
    follow_up_status: str

    model_config = {"from_attributes": True}


class StatusUpdate(BaseModel):
    status: FollowUpStatus
