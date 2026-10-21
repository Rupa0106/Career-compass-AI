from fastapi import APIRouter

router = APIRouter(
    prefix="/api/trends",
    tags=["Skill Trends"],
)

SKILL_TRENDS = [
    {
        "name": "Generative AI",
        "category": "AI",
        "description": "AI systems that generate text, images, code, and other content.",
        "level": "Beginner to Advanced",
    },
    {
        "name": "AI Agents",
        "category": "AI",
        "description": "Systems that use models and tools to perform multi-step tasks.",
        "level": "Intermediate",
    },
    {
        "name": "RAG",
        "category": "AI",
        "description": "Retrieval-Augmented Generation combines retrieval with language models.",
        "level": "Intermediate",
    },
    {
        "name": "Model Evaluation",
        "category": "AI",
        "description": "Methods for measuring AI system quality and reliability.",
        "level": "Intermediate",
    },
    {
        "name": "MCP",
        "category": "AI Infrastructure",
        "description": "A protocol for connecting AI applications with external tools and data.",
        "level": "Intermediate",
    },
]


@router.get("/")
def get_trends(category: str | None = None):
    if category:
        normalized = category.strip().lower()

        filtered_trends = [
            trend
            for trend in SKILL_TRENDS
            if normalized in trend["category"].lower()
        ]
    else:
        filtered_trends = SKILL_TRENDS

    return {
        "count": len(filtered_trends),
        "trends": filtered_trends,
    }