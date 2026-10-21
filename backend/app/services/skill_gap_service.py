CAREER_SKILLS = {
    "AI Engineer": [
        "Python",
        "SQL",
        "Machine Learning",
        "Data Processing",
        "Model Evaluation",
        "Generative AI",
    ],
    "Full Stack Developer": [
        "HTML",
        "CSS",
        "JavaScript",
        "React",
        "REST APIs",
        "SQL",
        "Backend Development",
    ],
    "Software Developer": [
        "Programming",
        "Data Structures",
        "Algorithms",
        "SQL",
        "Git",
        "Testing",
    ],
}


def analyze_skill_gap(
    career_goal: str,
    current_skills: list[str],
) -> dict:
    goal = career_goal.strip().lower()

    if "ai" in goal or "machine learning" in goal:
        target_skills = CAREER_SKILLS["AI Engineer"]
    elif "full stack" in goal or "web developer" in goal:
        target_skills = CAREER_SKILLS["Full Stack Developer"]
    else:
        target_skills = CAREER_SKILLS["Software Developer"]

    normalized_skills = {
        skill.strip().lower()
        for skill in current_skills
    }

    matched = [
        skill
        for skill in target_skills
        if skill.lower() in normalized_skills
    ]

    missing = [
        skill
        for skill in target_skills
        if skill.lower() not in normalized_skills
    ]

    score = round(
        len(matched) / len(target_skills) * 100
    )

    return {
        "career_goal": career_goal,
        "required_skills": target_skills,
        "matched_skills": matched,
        "missing_skills": missing,
        "coverage_percentage": score,
        "note": (
            "This is a simple skill-list comparison, "
            "not a validated measure of job readiness."
        ),
    }