from __future__ import annotations


def recommend_program(payload: dict[str, str]) -> tuple[str, str, str, str]:
    normalized = " ".join(payload.values()).lower()
    user_type = payload["user_type"].lower()
    ai_skill = payload["ai_skill_level"].lower()
    goal = payload["goal"].lower()

    if any(keyword in normalized for keyword in ["faculty", "teacher", "professor", "educator", "school", "college", "academic"]):
        return (
            "Faculty AI Training",
            "The profile indicates an education-focused context, so the recommendation emphasizes classroom-ready AI adoption, teaching workflows, and practical faculty use cases.",
            "Focus on lesson planning with AI, prompt design for educators, and policy-safe classroom use.",
            "Share a sample teaching workflow and book a faculty-specific orientation call.",
        )

    if any(keyword in normalized for keyword in ["company", "team", "corporate", "organization", "business", "hr", "department"]):
        return (
            "Corporate AI Training",
            "The inputs point to a team or organization setting, so the best fit is a practical corporate training path with workflow adoption and team enablement.",
            "Focus on internal use cases, governance, team enablement, and safe AI adoption across roles.",
            "Review team size, target workflows, and preferred delivery format for a training proposal.",
        )

    if any(keyword in goal for keyword in ["agent", "multi-agent", "automation workflow"]):
        return (
            "Agent Engineering Program",
            "The stated goal is oriented toward building AI agents and orchestration flows, which aligns with the agent engineering track.",
            "Strengthen tool use, orchestration design, evaluation, and reliability patterns for agentic systems.",
            "Start with a small agent prototype and a discovery call on the target automation use case.",
        )

    if any(keyword in goal for keyword in ["rag", "retrieval", "knowledge base", "document search", "search over documents"]):
        return (
            "RAG and Automation Program",
            "The goal centers on knowledge retrieval, document workflows, or automation, which maps directly to the RAG and automation track.",
            "Build skills in data preparation, retrieval design, prompt-grounding, and workflow automation.",
            "Prepare one document set or business workflow to scope a pilot project.",
        )

    if any(keyword in ai_skill for keyword in ["beginner", "new", "none", "basic"]) or any(keyword in goal for keyword in ["career", "job", "starter", "switch", "foundation"]):
        return (
            "AI Career Starter",
            "The profile suggests a foundational stage, so the career starter path offers a structured entry point with portfolio building and guided practice.",
            "Focus on AI fundamentals, prompt writing, simple projects, and portfolio-ready outcomes.",
            "Schedule an orientation and review the learner’s starting point, availability, and goals.",
        )

    if any(keyword in goal for keyword in ["build", "app", "product", "genai", "llm", "prototype"]):
        return (
            "GenAI Builder Program",
            "The goal is to build practical GenAI applications, making the builder track the most suitable default recommendation.",
            "Focus on APIs, prompt design, UI integration, evaluation, and shipping a small portfolio project.",
            "Plan a first project idea and validate the preferred learning mode before enrollment.",
        )

    if any(keyword in user_type for keyword in ["student", "individual", "learner", "job seeker"]):
        return (
            "AI Career Starter",
            "This looks like an individual learner profile with a broad entry-level fit, so the career starter path is the safest default.",
            "Start with fundamentals, practical AI usage, and guided portfolio projects.",
            "Run a short orientation and identify one target outcome for the first 30 days.",
        )

    return (
        "GenAI Builder Program",
        "The responses show enough interest in practical AI application to start with a builder-oriented path while keeping the scope flexible.",
        "Clarify the use case, fill any technical gaps, and choose a first project.",
        "Confirm the learner’s preferred project domain and set a follow-up call.",
    )
