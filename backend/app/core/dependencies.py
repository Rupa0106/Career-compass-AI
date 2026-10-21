from fastapi import Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.models.user import User
from app.routes.auth import get_current_user


def get_database_session(
    db: Session = Depends(get_db)
) -> Session:
    return db


def get_current_active_user(
    current_user: User = Depends(get_current_user)
) -> User:
    return current_user