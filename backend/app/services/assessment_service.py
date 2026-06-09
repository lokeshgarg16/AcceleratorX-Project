from __future__ import annotations

import json

from sqlalchemy.orm import Session

from ..models import Lead
from ..schemas import AssessmentCreate
from .gemini import generate_counsellor_notes
from .recommendation import recommend_program
from .scoring import score_lead


def process_assessment(db: Session, payload: AssessmentCreate) -> Lead:
    answer_map = payload.model_dump()
    program, reason, skill_gap, next_step = recommend_program(answer_map)
    score_result = score_lead(answer_map, program)

    recommendation = {
        "program": program,
        "reason": reason,
        "skill_gap": skill_gap,
        "next_step": next_step,
    }
    counsellor_notes = generate_counsellor_notes(answer_map, recommendation, score_result.total, score_result.category)

    lead = Lead(
        **answer_map,
        recommended_program=program,
        recommendation_reason=reason,
        readiness_level=score_result.readiness_level,
        skill_gap_summary=skill_gap,
        next_step=next_step,
        lead_score=score_result.total,
        category=score_result.category,
        follow_up_status="New",
        counsellor_notes=counsellor_notes,
        next_action=next_step,
        answers_json=json.dumps(answer_map, indent=2),
        score_breakdown=json.dumps(score_result.breakdown, indent=2),
    )
    db.add(lead)
    db.commit()
    db.refresh(lead)
    return lead
