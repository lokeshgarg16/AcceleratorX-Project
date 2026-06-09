from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class ScoreResult:
    total: int
    breakdown: dict[str, Any]
    category: str
    readiness_level: str


def _normalized(value: str) -> str:
    return value.strip().lower()


def _contains(value: str, options: list[str]) -> bool:
    normalized = _normalized(value)
    return any(option in normalized for option in options)


def score_goal_clarity(goal: str) -> int:
    normalized = _normalized(goal)
    score = 8
    if len(normalized) >= 20:
        score += 4
    if any(keyword in normalized for keyword in ["build", "create", "launch", "career", "transition", "learn", "portfolio", "project", "automation", "agent", "rag", "faculty", "team", "company"]):
        score += 8
    if any(keyword in normalized for keyword in ["specific", "want to", "looking to", "need help", "apply"]):
        score += 4
    return min(score, 20)


def score_background_relevance(current_role: str, education_background: str, ai_skill_level: str) -> int:
    score = 0
    role = _normalized(current_role)
    education = _normalized(education_background)
    skill = _normalized(ai_skill_level)

    if any(keyword in role for keyword in ["student", "developer", "engineer", "analyst", "teacher", "faculty", "manager", "founder"]):
        score += 6
    elif role:
        score += 4

    if any(keyword in education for keyword in ["computer", "engineering", "science", "technology", "data", "business", "education", "teaching"]):
        score += 5
    elif education:
        score += 3

    if any(keyword in skill for keyword in ["beginner", "intermediate", "advanced", "experienced"]):
        score += 4
    elif skill:
        score += 2

    return min(score, 15)


def score_budget_readiness(budget_readiness: str) -> int:
    if _contains(budget_readiness, ["ready", "can pay", "budget approved", "available"]):
        return 15
    if _contains(budget_readiness, ["partial", "need time", "exploring", "compare", "maybe"]):
        return 10
    if _contains(budget_readiness, ["scholar", "low", "not now", "later", "need support"]):
        return 5
    return 8 if budget_readiness.strip() else 0


def score_timeline_urgency(timeline: str) -> int:
    if _contains(timeline, ["immediately", "asap", "this month", "1 month", "urgent"]):
        return 15
    if _contains(timeline, ["2 months", "3 months", "this quarter", "soon"]):
        return 11
    if _contains(timeline, ["6 months", "exploring", "later", "sometime", "flexible"]):
        return 6
    return 8 if timeline.strip() else 0


def score_program_fit(user_type: str, current_role: str, goal: str, ai_skill_level: str) -> tuple[int, str]:
    normalized_text = " ".join([user_type, current_role, goal, ai_skill_level]).lower()
    score = 8
    if any(keyword in normalized_text for keyword in ["faculty", "teacher", "professor", "educator", "school", "college"]):
        score = 20
    elif any(keyword in normalized_text for keyword in ["company", "team", "corporate", "organization", "business", "hr"]):
        score = 18
    elif any(keyword in normalized_text for keyword in ["agent", "automation", "workflow"]):
        score = 18
    elif any(keyword in normalized_text for keyword in ["rag", "retrieval", "search", "knowledge base", "document"]):
        score = 17
    elif any(keyword in normalized_text for keyword in ["build", "app", "product", "genai", "llm"]):
        score = 15
    elif any(keyword in normalized_text for keyword in ["career", "job", "starter", "student", "beginner"]):
        score = 14
    return min(score, 20), _fit_reason(score, user_type, goal)


def _fit_reason(score: int, user_type: str, goal: str) -> str:
    if score >= 18:
        return f"The profile strongly matches the stated goal and learning context for {user_type.lower() or 'this learner'}."
    if score >= 14:
        return "The goal is aligned with a practical AcceleratorX path, though a short foundational step may still help."
    return "The current inputs suggest a general-fit route rather than a highly specialized program path."


def score_engagement_quality(weekly_availability: str, preferred_learning_mode: str) -> int:
    score = 4
    availability = _normalized(weekly_availability)
    learning_mode = _normalized(preferred_learning_mode)

    if any(keyword in availability for keyword in ["10", "12", "15", "20", "full", "high"]):
        score += 4
    elif any(keyword in availability for keyword in ["5", "6", "7", "8"]):
        score += 3
    elif availability:
        score += 2

    if any(keyword in learning_mode for keyword in ["live", "mentor", "project", "cohort", "blended"]):
        score += 3
    elif learning_mode:
        score += 2

    return min(score, 10)


def score_contact_completeness(contact_name: str, contact_email: str, contact_phone: str) -> int:
    complete_fields = sum(bool(field.strip()) for field in [contact_name, contact_email, contact_phone])
    if complete_fields == 3:
        return 5
    if complete_fields == 2:
        return 3
    if complete_fields == 1:
        return 1
    return 0


def score_lead(payload: dict[str, str], program_name: str) -> ScoreResult:
    goal_score = score_goal_clarity(payload["goal"])
    background_score = score_background_relevance(
        payload["current_role"],
        payload["education_background"],
        payload["ai_skill_level"],
    )
    budget_score = score_budget_readiness(payload["budget_readiness"])
    timeline_score = score_timeline_urgency(payload["timeline"])
    program_fit_score, fit_reason = score_program_fit(
        payload["user_type"],
        payload["current_role"],
        payload["goal"],
        payload["ai_skill_level"],
    )
    engagement_score = score_engagement_quality(payload["weekly_availability"], payload["preferred_learning_mode"])
    contact_score = score_contact_completeness(
        payload["contact_name"],
        payload["contact_email"],
        payload["contact_phone"],
    )

    total = min(goal_score + background_score + budget_score + timeline_score + program_fit_score + engagement_score + contact_score, 100)

    if total >= 80:
        category = "Hot"
        readiness_level = "High readiness"
    elif total >= 60:
        category = "Warm"
        readiness_level = "Moderate readiness"
    elif total >= 40:
        category = "Cold"
        readiness_level = "Early readiness"
    else:
        category = "Not Suitable"
        readiness_level = "Needs foundational support"

    breakdown = {
        "goal_clarity": goal_score,
        "background_relevance": background_score,
        "budget_readiness": budget_score,
        "timeline_urgency": timeline_score,
        "program_fit": program_fit_score,
        "engagement_quality": engagement_score,
        "contact_completeness": contact_score,
        "fit_reason": fit_reason,
        "program_context": program_name,
    }

    return ScoreResult(total=total, breakdown=breakdown, category=category, readiness_level=readiness_level)
