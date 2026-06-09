from __future__ import annotations

import os

try:
    import google.generativeai as genai
except Exception:  # pragma: no cover - optional dependency fallback
    genai = None


def build_counsellor_prompt(payload: dict[str, str], recommendation: dict[str, str]) -> str:
    return f"""
You are a senior admissions counsellor for AcceleratorX.

Write concise counsellor notes based on the learner profile below.

Safety rules:
- Do not guarantee jobs, salary, internships, or placements.
- Use safe language like career support, portfolio guidance, project support, and placement assistance.
- Be practical, explainable, and action-oriented.

Learner profile:
User type: {payload['user_type']}
Current role: {payload['current_role']}
Education/background: {payload['education_background']}
AI skill level: {payload['ai_skill_level']}
Goal: {payload['goal']}
Timeline: {payload['timeline']}
Budget readiness: {payload['budget_readiness']}
Weekly availability: {payload['weekly_availability']}
Preferred learning mode: {payload['preferred_learning_mode']}
Contact name: {payload['contact_name']}

Recommendation:
Program: {recommendation['program']}
Reason: {recommendation['reason']}
Skill gaps: {recommendation['skill_gap']}
Next step: {recommendation['next_step']}

Return 3 short sections:
1. Summary of fit
2. Key support areas
3. Suggested counsellor action
""".strip()


def generate_counsellor_notes(payload: dict[str, str], recommendation: dict[str, str], score: int, category: str) -> str:
    api_key = os.getenv("GEMINI_API_KEY", "").strip()
    model_name = os.getenv("GEMINI_MODEL", "gemini-1.5-flash").strip()

    if not api_key or genai is None:
        return _fallback_notes(recommendation, score, category)

    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel(model_name)
        prompt = build_counsellor_prompt(payload, recommendation)
        response = model.generate_content(prompt)
        text = getattr(response, "text", "").strip()
        return text or _fallback_notes(recommendation, score, category)
    except Exception:
        return _fallback_notes(recommendation, score, category)


def _fallback_notes(recommendation: dict[str, str], score: int, category: str) -> str:
    return (
        f"Summary of fit:\n"
        f"- Lead score: {score}/100 ({category})\n"
        f"- Recommended program: {recommendation['program']}\n\n"
        f"Key support areas:\n"
        f"- {recommendation['skill_gap']}\n"
        f"- Review timeline, budget readiness, and weekly availability before enrollment\n\n"
        f"Suggested counsellor action:\n"
        f"- {recommendation['next_step']}\n"
        f"- Keep the conversation focused on career support, project support, and placement assistance rather than guaranteed outcomes."
    )
