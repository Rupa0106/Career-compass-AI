ROADMAP_TEMPLATES = {
    "AI Engineer": [
        {
            "stage": "Foundation",
            "topics": [
                "Python programming",
                "Git and GitHub",
                "Basic mathematics for AI",
                "SQL fundamentals",
            ],
        },
        {
            "stage": "Intermediate",
            "topics": [
                "NumPy and Pandas",
                "Data visualization",
                "Machine learning fundamentals",
                "Model evaluation",
            ],
        },
        {
            "stage": "Advanced",
            "topics": [
                "Deep learning fundamentals",
                "Natural language processing",
                "Large language models",
                "Retrieval-Augmented Generation",
            ],
        },
        {
            "stage": "Job-ready",
            "topics": [
                "Build an AI application",
                "Create a REST API with FastAPI",
                "Deploy a project",
                "Prepare a GitHub portfolio",
            ],
        },
    ],
    "Full Stack Developer": [
        {
            "stage": "Foundation",
            "topics": [
                "HTML",
                "CSS",
                "JavaScript fundamentals",
                "Git and GitHub",
            ],
        },
        {
            "stage": "Intermediate",
            "topics": [
                "Responsive web design",
                "JavaScript DOM",
                "React fundamentals",
                "REST APIs",
            ],
        },
        {
            "stage": "Advanced",
            "topics": [
                "Python and FastAPI",
                "SQL and database design",
                "Authentication",
                "Frontend-backend integration",
            ],
        },
        {
            "stage": "Job-ready",
            "topics": [
                "Build a full-stack project",
                "Testing and debugging",
                "Deployment",
                "Portfolio and interview preparation",
            ],
        },
    ],
    "Software Developer": [
        {
            "stage": "Foundation",
            "topics": [
                "Python or Java fundamentals",
                "Problem-solving",
                "Data structures",
                "Git and GitHub",
            ],
        },
        {
            "stage": "Intermediate",
            "topics": [
                "Data structures and algorithms",
                "Object-oriented programming",
                "SQL",
                "API fundamentals",
            ],
        },
        {
            "stage": "Advanced",
            "topics": [
                "Backend development",
                "Software design principles",
                "Automated testing",
                "System design fundamentals",
            ],
        },
        {
            "stage": "Job-ready",
            "topics": [
                "Build portfolio projects",
                "Practice coding interviews",
                "Write a technical resume",
                "Prepare for technical interviews",
            ],
        },
    ],
}


def generate_roadmap(
    career_goal: str,
    current_skills: list[str] | None = None,
) -> dict:
    normalized_goal = career_goal.strip().lower()

    if "ai" in normalized_goal or "machine learning" in normalized_goal:
        template_key = "AI Engineer"
    elif "full stack" in normalized_goal or "web developer" in normalized_goal:
        template_key = "Full Stack Developer"
    else:
        template_key = "Software Developer"

    known_skills = {
        skill.strip().lower()
        for skill in (current_skills or [])
        if skill.strip()
    }

    stages = []

    for template_stage in ROADMAP_TEMPLATES[template_key]:
        topics = []

        for topic in template_stage["topics"]:
            topics.append({
                "title": topic,
                "completed": topic.lower() in known_skills,
                "resources": [],
            })

        stages.append({
            "stage": template_stage["stage"],
            "topics": topics,
        })

    return {
        "title": f"{career_goal.strip()} Learning Roadmap",
        "career_goal": career_goal.strip(),
        "stages": stages,
        "progress": 0,
    }