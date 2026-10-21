from typing import List

from pydantic import BaseModel, Field, ConfigDict


class ProfileUpdate(BaseModel):
    branch: str = Field(default="CSE", max_length=100)
    study_year: int = Field(default=1, ge=1, le=4)

    current_skills: List[str] = Field(default_factory=list)
    interests: List[str] = Field(default_factory=list)

    career_goal: str = Field(
        default="Software Developer",
        max_length=150
    )

    weekly_study_hours: int = Field(
        default=10,
        ge=0,
        le=168
    )


class ProfileResponse(BaseModel):
    id: int
    user_id: int
    branch: str
    study_year: int
    current_skills: List[str]
    interests: List[str]
    career_goal: str
    weekly_study_hours: int

    model_config = ConfigDict(from_attributes=True)