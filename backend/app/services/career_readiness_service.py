from app.services.skill_gap_service import analyze_skill_gap


def calculate_career_readiness(
    career_goal: str,
    current_skills: list[str],
) -> dict:
    """
    Estimate career readiness using skill coverage.
    This is an indicative score, not a job guarantee.
    """

    result = analyze_skill_gap(
        career_goal=career_goal,
        current_skills=current_skills,
    )

    coverage = result.get("coverage_percentage", 0)

    if coverage >= 80:
        level = "Strong Skill Coverage"
    elif coverage >= 50:
        level = "Developing"
    else:
        level = "Needs More Preparation"

    return {
        "career_goal": career_goal,
        "readiness_percentage": coverage,
        "readiness_level": level,
        "required_skills": result.get("required_skills", []),
        "matched_skills": result.get("matched_skills", []),
        "missing_skills": result.get("missing_skills", []),
        "message": (
            "This score estimates skill coverage only. "
            "It does not guarantee job placement."
        ),
    }