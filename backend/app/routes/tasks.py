from datetime import date

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.models.task import Task
from app.models.user import User
from app.routes.auth import get_current_user

router = APIRouter(prefix="/api/tasks", tags=["Study Tasks"])


class TaskCreate(BaseModel):
    title: str = Field(min_length=2, max_length=200)
    description: str = Field(default="", max_length=1000)
    due_date: date | None = None


class TaskUpdate(BaseModel):
    is_completed: bool


class TaskResponse(BaseModel):
    id: int
    title: str
    description: str
    due_date: date | None
    is_completed: bool

    model_config = {"from_attributes": True}


@router.post("/", response_model=TaskResponse)
def create_task(
    data: TaskCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    task = Task(
        user_id=current_user.id,
        title=data.title,
        description=data.description,
        due_date=data.due_date,
    )

    db.add(task)
    db.commit()
    db.refresh(task)

    return task


@router.get("/", response_model=list[TaskResponse])
def list_tasks(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return db.query(Task).filter(
        Task.user_id == current_user.id
    ).order_by(Task.id.desc()).all()


@router.patch("/{task_id}", response_model=TaskResponse)
def update_task(
    task_id: int,
    data: TaskUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    task = db.query(Task).filter(
        Task.id == task_id,
        Task.user_id == current_user.id,
    ).first()

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found.",
        )

    task.is_completed = data.is_completed

    db.commit()
    db.refresh(task)

    return task


@router.delete("/{task_id}")
def delete_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    task = db.query(Task).filter(
        Task.id == task_id,
        Task.user_id == current_user.id,
    ).first()

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found.",
        )

    db.delete(task)
    db.commit()

    return {"message": "Task deleted successfully."}