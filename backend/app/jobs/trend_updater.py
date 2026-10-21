from datetime import datetime, timezone


def refresh_skill_trends() -> dict:
    """
    Return a curated list of technology trends.

    This is sample data, not a live market update.
    """

    trends = [
        {
            "name": "Generative AI",
            "category": "Artificial Intelligence",
            "description": "AI models that generate text, images and other content."
        },
        {
            "name": "AI Agents",
            "category": "Artificial Intelligence",
            "description": "AI systems that can perform multi-step tasks."
        },
        {
            "name": "RAG",
            "category": "AI Engineering",
            "description": "Combining retrieval with language models."
        },
        {
            "name": "Model Evaluation",
            "category": "AI Engineering",
            "description": "Testing AI systems for quality and reliability."
        },
        {
            "name": "MCP",
            "category": "AI Tools",
            "description": "A protocol for connecting AI applications with tools and data."
        }
    ]

    return {
        "updated_at": datetime.now(timezone.utc).isoformat(),
        "source": "curated_sample_data",
        "trends": trends
    }


if __name__ == "__main__":
    result = refresh_skill_trends()

    print("CareerCompass AI - Skill Trends")
    print("Updated at:", result["updated_at"])

    for trend in result["trends"]:
        print(f"- {trend['name']}: {trend['description']}")