from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database.connection import Base, engine

# Import models so SQLAlchemy registers all tables
from app import models

# Import API routers
from app.routes import (
    auth,
    profiles,
    roadmaps,
    skills,
    trends,
    tasks,
    resources,
    projects,
    certificates,
    analytics,
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Create database tables when the application starts
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(
    title="CareerCompass AI API",
    description=(
        "Personalized career roadmaps, skill-gap analysis, "
        "learning resources, projects, and career readiness."
    ),
    version="1.0.0",
    lifespan=lifespan,
)


# Allow the frontend to communicate with the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:8000",
        "http://localhost:8000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Register API routers
app.include_router(auth.router)
app.include_router(profiles.router)
app.include_router(roadmaps.router)
app.include_router(skills.router)
app.include_router(trends.router)
app.include_router(tasks.router)
app.include_router(resources.router)
app.include_router(projects.router)
app.include_router(certificates.router)
app.include_router(analytics.router)


@app.get("/")
def home():
    return {
        "message": "Welcome to CareerCompass AI API",
        "status": "running",
        "docs": "/docs",
    }


@app.get("/health")
def health_check():
    return {"status": "healthy"}