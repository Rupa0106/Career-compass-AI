from pydantic import BaseModel, Field, ConfigDict


class SkillCreate(BaseModel):
    name: str = Field(
        ...,
        min_length=2,
        max_length=100
    )

    category: str = Field(
        ...,
        min_length=2,
        max_length=100
    )

    level: str = Field(
        default="Beginner",
        max_length=50
    )

    description: str = Field(
        default="",
        max_length=500
    )


class SkillResponse(BaseModel):
    id: int
    name: str
    category: str
    level: str
    description: str

    model_config = ConfigDict(from_attributes=True)