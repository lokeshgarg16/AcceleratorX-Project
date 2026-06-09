from __future__ import annotations

import json

from sqlalchemy.orm import Session

from .models import Lead


def _lead(answer_map: dict[str, str], recommendation: dict[str, str], score: int, category: str, readiness_level: str) -> Lead:
    return Lead(
        **answer_map,
        recommended_program=recommendation["program"],
        recommendation_reason=recommendation["reason"],
        readiness_level=readiness_level,
        skill_gap_summary=recommendation["skill_gap"],
        next_step=recommendation["next_step"],
        lead_score=score,
        category=category,
        follow_up_status="New",
        counsellor_notes=recommendation["notes"],
        next_action=recommendation["next_step"],
        answers_json=json.dumps(answer_map, indent=2),
        score_breakdown=json.dumps(recommendation["score_breakdown"], indent=2),
    )


def seed_demo_leads(db: Session) -> None:
    if db.query(Lead).count() > 0:
        return

    demo_leads = [
        _lead(
            {
                "user_type": "Student",
                "current_role": "Final year computer science student",
                "education_background": "Computer Science undergraduate with projects in Python and web apps",
                "ai_skill_level": "Beginner",
                "goal": "I want to build a strong AI portfolio and move into an AI career path",
                "timeline": "Within 1-3 months",
                "budget_readiness": "I can pay with some planning",
                "weekly_availability": "8-10 hours",
                "preferred_learning_mode": "Live cohorts with projects",
                "contact_name": "Aarav Sharma",
                "contact_email": "aarav@example.com",
                "contact_phone": "9876543210",
            },
            {
                "program": "AI Career Starter",
                "reason": "The learner is early-stage and looking for a structured AI entry path with portfolio support.",
                "skill_gap": "Focus on fundamentals, prompt writing, and one guided starter project.",
                "next_step": "Book an orientation call and map the first 30-day learning plan.",
                "notes": "Strong foundational fit. Recommend a starter conversation that keeps expectations practical and centers on portfolio guidance, project support, and placement assistance rather than outcome guarantees.",
                "score_breakdown": {
                    "goal_clarity": 17,
                    "background_relevance": 12,
                    "budget_readiness": 10,
                    "timeline_urgency": 11,
                    "program_fit": 14,
                    "engagement_quality": 8,
                    "contact_completeness": 5,
                },
            },
            77,
            "Warm",
            "Moderate readiness",
        ),
        _lead(
            {
                "user_type": "Corporate team",
                "current_role": "Operations manager",
                "education_background": "MBA in operations and process management",
                "ai_skill_level": "Intermediate",
                "goal": "We want to train our team on practical AI workflows for internal productivity",
                "timeline": "This quarter",
                "budget_readiness": "Budget is approved",
                "weekly_availability": "5 hours",
                "preferred_learning_mode": "Blended workshop format",
                "contact_name": "Neha Iyer",
                "contact_email": "neha@company.com",
                "contact_phone": "9123456780",
            },
            {
                "program": "Corporate AI Training",
                "reason": "The lead represents a team context with a clear organizational use case, which aligns with corporate enablement.",
                "skill_gap": "Clarify internal use cases, governance, and team rollout priorities.",
                "next_step": "Share team size, target workflows, and preferred delivery format for a proposal.",
                "notes": "Good corporate fit. Keep the discussion focused on workflow automation, safe adoption, and team enablement. Avoid any promise of business outcomes.",
                "score_breakdown": {
                    "goal_clarity": 18,
                    "background_relevance": 13,
                    "budget_readiness": 15,
                    "timeline_urgency": 11,
                    "program_fit": 18,
                    "engagement_quality": 7,
                    "contact_completeness": 5,
                },
            },
            87,
            "Hot",
            "High readiness",
        ),
        _lead(
            {
                "user_type": "Independent learner",
                "current_role": "Freelance designer",
                "education_background": "Design diploma with some no-code experience",
                "ai_skill_level": "Basic",
                "goal": "I want to understand AI before I decide which program to join",
                "timeline": "6 months",
                "budget_readiness": "Not ready yet",
                "weekly_availability": "3-4 hours",
                "preferred_learning_mode": "Self-paced with occasional guidance",
                "contact_name": "Riya Patel",
                "contact_email": "riya@example.com",
                "contact_phone": "9988776655",
            },
            {
                "program": "AI Career Starter",
                "reason": "The learner needs a foundational path because the goal is exploratory and the skill level is still basic.",
                "skill_gap": "Build AI fundamentals and a small project before moving into a more advanced program.",
                "next_step": "Nudge toward a starter orientation and clarify the first tangible learning outcome.",
                "notes": "Early-stage fit. Counsellor should focus on foundational support, learning expectations, and a practical starter path without implying job outcomes.",
                "score_breakdown": {
                    "goal_clarity": 10,
                    "background_relevance": 7,
                    "budget_readiness": 5,
                    "timeline_urgency": 6,
                    "program_fit": 14,
                    "engagement_quality": 5,
                    "contact_completeness": 5,
                },
            },
            52,
            "Cold",
            "Early readiness",
        ),
    ]

    db.add_all(demo_leads)
    db.commit()
