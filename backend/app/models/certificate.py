from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.connection import Base


class Certificate(Base):
    __tablename__ = "certificates"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    title: Mapped[str] = mapped_column(
        String(200),
        nullable=False,
    )

    issuer: Mapped[str] = mapped_column(
        String(200),
        nullable=False,
    )

    certificate_url: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
    )

    issue_date: Mapped[str | None] = mapped_column(
        String(30),
        nullable=True,
    )

    user = relationship(
        "User",
        back_populates="certificates",
    )