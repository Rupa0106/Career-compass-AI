from typing import Any

from pydantic import BaseModel, Field, ConfigDict


class RoadmapGenerateRequest(BaseModel):
    career_goal: str = Field(
        default="Software Developer",
        min_length=2,
        max_length=150,
    )

    current_skills: list[str] = Field(
        default_factory=list,
    )


class RoadmapResponse(BaseModel):
    id: int
    user_id: int
    title: str
    career_goal: str
    stages: list[dict[str, Any]]
    progress: int = Field(ge=0, le=100)

    model_config = ConfigDict(from_attributes=True)