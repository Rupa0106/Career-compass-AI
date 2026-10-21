# CareerCompass AI - Backend

## 1. Project Overview

CareerCompass AI is a personalized career guidance platform
that helps students plan their learning journey.

The backend provides APIs for user authentication, student profiles,
career roadmaps, skill analysis, learning tasks, projects,
certificates, and dashboard analytics.

## 2. Technology Stack

- Python
- FastAPI
- Uvicorn
- SQLAlchemy
- SQLite
- Pydantic
- JWT Authentication

## 3. Backend Architecture

The backend is organized into the following modules:

- core: Configuration, security, and dependencies.
- database: Database connection and SQLAlchemy Base.
- models: Database table definitions.
- schemas: API request and response validation.
- routes: API endpoints.
- services: Business logic.
- jobs: Background or scheduled job-related logic.

## 4. Installation

Open PowerShell in the backend directory.

Activate the project virtual environment from the project root:

```powershell
..\.venv\Scripts\Activate.ps1