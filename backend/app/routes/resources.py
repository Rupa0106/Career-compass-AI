from fastapi import APIRouter

router = APIRouter(prefix="/api/resources", tags=["Learning Resources"])


RESOURCES = [
    {
        "topic": "Python",
        "title": "Official Python Tutorial",
        "url": "https://docs.python.org/3/tutorial/",
        "type": "Documentation",
    },
    {
        "topic": "Web Development",
        "title": "MDN Web Docs",
        "url": "https://developer.mozilla.org/",
        "type": "Documentation",
    },
    {
        "topic": "SQL",
        "title": "SQLBolt",
        "url": "https://sqlbolt.com/",
        "type": "Interactive Tutorial",
    },
    {
        "topic": "Git",
        "title": "Git Documentation",
        "url": "https://git-scm.com/doc",
        "type": "Documentation",
    },
    {
        "topic": "AI",
        "title": "Google Machine Learning Crash Course",
        "url": "https://developers.google.com/machine-learning/crash-course",
        "type": "Course",
    },
]


@router.get("/")
def list_resources(topic: str | None = None):
    if topic:
        normalized = topic.strip().lower()

        filtered = [
            resource
            for resource in RESOURCES
            if normalized in resource["topic"].lower()
        ]

        return {"resources": filtered}

    return {"resources": RESOURCES}