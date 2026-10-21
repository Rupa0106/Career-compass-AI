# CareerCompass AI - System Architecture

## 1. Project Overview

CareerCompass AI is a personalized career guidance platform
designed for B.Tech students, beginners, and self-learners.

The platform helps users identify what skills they need to learn,
create career roadmaps, access learning resources, and track progress.

## 2. Main Objectives

- Provide personalized career roadmaps.
- Identify missing skills for a target career.
- Recommend free learning resources.
- Track daily learning tasks and progress.
- Display emerging AI skills and technology trends.
- Help students organize projects and certificates.
- Estimate career readiness based on skill coverage.

## 3. Technology Stack

### Frontend
- HTML5
- CSS3
- JavaScript

### Backend
- Python
- FastAPI
- Uvicorn

### Database
- SQLite
- SQLAlchemy ORM

### Authentication and Security
- Password hashing
- JWT-based authentication
- Request validation using Pydantic
- Authenticated API endpoints

### AI Integration
- Rule-based roadmap fallback
- External AI API integration planned

## 4. System Architecture

```text
                 USER
                  |
                  v
       FRONTEND - HTML/CSS/JS
                  |
                  v
          FASTAPI BACKEND
                  |
       +----------+----------+
       |          |          |
       v          v          v
    ROUTES     SERVICES   SECURITY
       |          |          |
       +----------+----------+
                  |
                  v
           SQLALCHEMY ORM
                  |
                  v
              SQLITE DB