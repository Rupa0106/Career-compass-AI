import os


def generate_ai_roadmap(
    career_goal: str,
    current_skills: list[str],
    study_hours_per_week: int = 10
) -> dict:
    """
    Generate a basic roadmap structure.

    This version uses a fallback roadmap.
    An external AI API can be integrated later.
    """

    goal = career_goal.strip().lower()

    if "ai" in goal or "machine learning" in goal:
        stages = {
            "Foundation": [
                "Python basics",
                "Mathematics for AI",
                "SQL fundamentals"
            ],
            "Intermediate": [
                "NumPy and Pandas",
                "Machine Learning",
                "Data Visualization"
            ],
            "Advanced": [
                "Deep Learning",
                "Generative AI",
                "Retrieval-Augmented Generation (RAG)"
            ],
            "Job-ready": [
                "Build AI projects",
                "Create a GitHub portfolio",
                "Practice interview questions"
            ]
        }

    elif "full stack" in goal:
        stages = {
            "Foundation": [
                "HTML",
                "CSS",
                "JavaScript"
            ],
            "Intermediate": [
                "Python",
                "FastAPI",
                "SQL and databases"
            ],
            "Advanced": [
                "React",
                "REST APIs",
                "Authentication"
            ],
            "Job-ready": [
                "Build a full-stack project",
                "Deploy the project",
                "Prepare for interviews"
            ]
        }

    else:
        stages = {
            "Foundation": [
                "Programming fundamentals",
                "Data Structures basics",
                "Git and GitHub"
            ],
            "Intermediate": [
                "Data Structures and Algorithms",
                "Object-Oriented Programming",
                "SQL"
            ],
            "Advanced": [
                "Backend development",
                "REST APIs",
                "Software design fundamentals"
            ],
            "Job-ready": [
                "Build projects",
                "Create a portfolio",
                "Practice technical interviews"
            ]
        }

    return {
        "career_goal": career_goal,
        "current_skills": current_skills,
        "study_hours_per_week": study_hours_per_week,
        "stages": stages,
        "generation_method": "fallback"
    }