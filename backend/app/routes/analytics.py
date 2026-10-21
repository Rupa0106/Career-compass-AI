from fastapi import APIRouter, Depends
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.models.user import User
from app.models.roadmap import Roadmap
from app.models.task import Task
from app.models.project import Project
from app.routes.auth import get_current_user

from app.services.skill_gap_service import analyze_skill_gap
from app.services.career_readiness_service import (
    calculate_career_readiness,
)

router = APIRouter(
    prefix="/api/analytics",
    tags=["Analytics"],
)


class SkillAnalysisRequest(BaseModel):
    career_goal: str = Field(
        default="Software Developer",
        min_length=2,
        max_length=100,
    )
    current_skills: list[str] = Field(default_factory=list)


# 1. Skill Gap Analysis
@router.post("/skill-gap")
def get_skill_gap(
    request: SkillAnalysisRequest,
    current_user: User = Depends(get_current_user),
):
    result = analyze_skill_gap(
        career_goal=request.career_goal,
        current_skills=request.current_skills,
    )

    return {
        "user_id": current_user.id,
        "analysis": result,
    }


# 2. Career Readiness Analysis
@router.post("/career-readiness")
def get_career_readiness(
    request: SkillAnalysisRequest,
    current_user: User = Depends(get_current_user),
):
    result = calculate_career_readiness(
        career_goal=request.career_goal,
        current_skills=request.current_skills,
    )

    return {
        "user_id": current_user.id,
        "career_readiness": result,
    }


# 3. Dashboard Statistics
@router.get("/dashboard")
def get_dashboard_analytics(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    roadmaps_count = (
        db.query(Roadmap)
        .filter(Roadmap.user_id == current_user.id)
        .count()
    )

    projects_count = (
        db.query(Project)
        .filter(Project.user_id == current_user.id)
        .count()
    )

    tasks_query = db.query(Task).filter(
        Task.user_id == current_user.id
    )

    total_tasks = tasks_query.count()

    completed_tasks = tasks_query.filter(
        Task.is_completed.is_(True)
    ).count()

    pending_tasks = total_tasks - completed_tasks

    completion_percentage = (
        round((completed_tasks / total_tasks) * 100, 2)
        if total_tasks > 0
        else 0
    )

    return {
        "user_id": current_user.id,
        "statistics": {
            "total_roadmaps": roadmaps_count,
            "total_projects": projects_count,
            "total_tasks": total_tasks,
            "completed_tasks": completed_tasks,
            "pending_tasks": pending_tasks,
            "task_completion_percentage": completion_percentage,
        },
    }