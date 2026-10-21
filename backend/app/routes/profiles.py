from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.models.profile import StudentProfile
from app.routes.auth import get_current_user
from app.schemas.profile import ProfileUpdate, ProfileResponse

router = APIRouter(prefix="/api/profiles", tags=["Student Profile"])


@router.get("/me", response_model=ProfileResponse | None)
def get_my_profile(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return (
        db.query(StudentProfile)
        .filter(StudentProfile.user_id == current_user.id)
        .first()
    )


@router.put("/me", response_model=ProfileResponse)
def update_my_profile(
    data: ProfileUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    profile = (
        db.query(StudentProfile)
        .filter(StudentProfile.user_id == current_user.id)
        .first()
    )

    if profile is None:
        profile = StudentProfile(user_id=current_user.id)
        db.add(profile)

    profile.branch = data.branch
    profile.study_year = data.study_year
    profile.current_skills = data.current_skills
    profile.interests = data.interests
    profile.career_goal = data.career_goal
    profile.weekly_study_hours = data.weekly_study_hours

    db.commit()
    db.refresh(profile)

    return profile
