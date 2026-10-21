from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.models.project import Project
from app.routes.auth import get_current_user

router = APIRouter(prefix="/api/projects", tags=["Portfolio Projects"])


class ProjectCreate(BaseModel):
    title: str = Field(min_length=1, max_length=150)
    description: str = Field(default="", max_length=2000)
    tech_stack: list[str] = Field(default_factory=list)
    github_url: str | None = None
    live_url: str | None = None


class ProjectResponse(BaseModel):
    id: int
    title: str
    description: str
    tech_stack: list[str]
    github_url: str | None
    live_url: str | None

    model_config = {"from_attributes": True}


@router.post("/", response_model=ProjectResponse)
def create_project(
    data: ProjectCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    project = Project(
        user_id=current_user.id,
        title=data.title,
        description=data.description,
        tech_stack=data.tech_stack,
        github_url=data.github_url,
        live_url=data.live_url,
    )

    db.add(project)
    db.commit()
    db.refresh(project)

    return project


@router.get("/", response_model=list[ProjectResponse])
def list_projects(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return (
        db.query(Project)
        .filter(Project.user_id == current_user.id)
        .all()
    )


@router.delete("/{project_id}")
def delete_project(
    project_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    project = (
        db.query(Project)
        .filter(
            Project.id == project_id,
            Project.user_id == current_user.id,
        )
        .first()
    )

    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")

    db.delete(project)
    db.commit()

    return {"message": "Project deleted successfully"}