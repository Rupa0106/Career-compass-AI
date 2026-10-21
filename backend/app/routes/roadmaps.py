from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.models.roadmap import Roadmap
from app.models.user import User
from app.routes.auth import get_current_user
from app.schemas.roadmap import (
    RoadmapGenerateRequest,
    RoadmapResponse,
)
from app.services.roadmap_service import generate_roadmap

router = APIRouter(prefix="/api/roadmaps", tags=["Roadmaps"])


@router.post("/generate", response_model=RoadmapResponse)
def create_roadmap(
    data: RoadmapGenerateRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    generated = generate_roadmap(
        data.career_goal,
        data.current_skills,
    )

    roadmap = Roadmap(
        user_id=current_user.id,
        title=generated["title"],
        career_goal=generated["career_goal"],
        stages=generated["stages"],
        progress=generated["progress"],
    )

    db.add(roadmap)
    db.commit()
    db.refresh(roadmap)

    return roadmap


@router.get("/", response_model=list[RoadmapResponse])
def list_roadmaps(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return db.query(Roadmap).filter(
        Roadmap.user_id == current_user.id
    ).order_by(Roadmap.id.desc()).all()


@router.get("/{roadmap_id}", response_model=RoadmapResponse)
def get_roadmap(
    roadmap_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    roadmap = db.query(Roadmap).filter(
        Roadmap.id == roadmap_id,
        Roadmap.user_id == current_user.id,
    ).first()

    if roadmap is None:
        raise HTTPException(
            status_code=404,
            detail="Roadmap not found.",
        )

    return roadmap