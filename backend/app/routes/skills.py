from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.models.skill import Skill

router = APIRouter(
    prefix="/api/skills",
    tags=["Skills"],
)


@router.get("/")
def list_skills(
    category: str | None = None,
    search: str | None = None,
    db: Session = Depends(get_db),
):
    query = db.query(Skill)

    if category:
        query = query.filter(
            Skill.category.ilike(f"%{category.strip()}%")
        )

    if search:
        query = query.filter(
            Skill.name.ilike(f"%{search.strip()}%")
        )

    skills = query.order_by(Skill.name.asc()).all()

    return {
        "count": len(skills),
        "skills": [
            {
                "id": skill.id,
                "name": skill.name,
                "category": skill.category,
                "level": skill.level,
                "description": skill.description,
            }
            for skill in skills
        ],
    }


@router.get("/{skill_id}")
def get_skill(
    skill_id: int,
    db: Session = Depends(get_db),
):
    skill = db.query(Skill).filter(
        Skill.id == skill_id
    ).first()

    if skill is None:
        from fastapi import HTTPException
        raise HTTPException(
            status_code=404,
            detail="Skill not found.",
        )

    return {
        "id": skill.id,
        "name": skill.name,
        "category": skill.category,
        "level": skill.level,
        "description": skill.description,
    }