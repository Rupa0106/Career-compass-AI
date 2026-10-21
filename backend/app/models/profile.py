from sqlalchemy import Column, Integer, String, ForeignKey, JSON
from sqlalchemy.orm import relationship

from app.database.connection import Base


class StudentProfile(Base):
    __tablename__ = "student_profiles"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id", ondelete="CASCADE"),
        unique=True,
        nullable=False
    )

    branch = Column(String(100), default="CSE")
    study_year = Column(Integer, default=1)

    current_skills = Column(JSON, default=list, nullable=False)
    interests = Column(JSON, default=list, nullable=False)

    career_goal = Column(
        String(150),
        default="Software Developer"
    )

    weekly_study_hours = Column(Integer, default=10)

    user = relationship(
        "User",
        back_populates="profile"
    )