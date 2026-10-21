from sqlalchemy import Column, Integer, String, Text
from app.database.connection import Base


class Skill(Base):
    __tablename__ = "skills"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(
        String(100),
        unique=True,
        nullable=False,
        index=True
    )

    category = Column(
        String(100),
        nullable=False
    )

    level = Column(
        String(50),
        default="Beginner",
        nullable=False
    )

    description = Column(
        Text,
        nullable=True
    )

    def __repr__(self):
        return f"<Skill(name='{self.name}', category='{self.category}')>"