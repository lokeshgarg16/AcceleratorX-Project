from __future__ import annotations

from datetime import datetime, timezone

from sqlalchemy import DateTime, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from .database import Base


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


class Lead(Base):
    __tablename__ = "leads"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utc_now)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utc_now, onupdate=utc_now)

    user_type: Mapped[str] = mapped_column(String(120), index=True)
    current_role: Mapped[str] = mapped_column(String(160))
    education_background: Mapped[str] = mapped_column(Text)
    ai_skill_level: Mapped[str] = mapped_column(String(80))
    goal: Mapped[str] = mapped_column(Text)
    timeline: Mapped[str] = mapped_column(String(80))
    budget_readiness: Mapped[str] = mapped_column(String(120))
    weekly_availability: Mapped[str] = mapped_column(String(80))
    preferred_learning_mode: Mapped[str] = mapped_column(String(120))
    contact_name: Mapped[str] = mapped_column(String(160))
    contact_email: Mapped[str] = mapped_column(String(255))
    contact_phone: Mapped[str] = mapped_column(String(50))

    recommended_program: Mapped[str] = mapped_column(String(120), index=True)
    recommendation_reason: Mapped[str] = mapped_column(Text)
    readiness_level: Mapped[str] = mapped_column(String(120))
    skill_gap_summary: Mapped[str] = mapped_column(Text)
    next_step: Mapped[str] = mapped_column(Text)

    lead_score: Mapped[int] = mapped_column(Integer, index=True)
    category: Mapped[str] = mapped_column(String(40), index=True)
    follow_up_status: Mapped[str] = mapped_column(String(40), default="New", index=True)

    counsellor_notes: Mapped[str] = mapped_column(Text)
    next_action: Mapped[str] = mapped_column(Text)
    answers_json: Mapped[str] = mapped_column(Text)
    score_breakdown: Mapped[str] = mapped_column(Text)
