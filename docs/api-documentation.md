
---

## 2. `api-documentation.md`

**File path:**
`CareerCompassAI/docs/api-documentation.md`

Ee content paste cheyyi:

```markdown
# CareerCompass AI - API Documentation

## 1. Introduction

The CareerCompass AI backend uses FastAPI to provide REST APIs.

Base URL during local development:

http://127.0.0.1:8000

Interactive API documentation is available at:

http://127.0.0.1:8000/docs

These URLs work when the backend server is running on port 8000.

## 2. Authentication

Protected endpoints require a valid access token.

For authenticated requests, send this HTTP header:

Authorization: Bearer YOUR_ACCESS_TOKEN

Replace YOUR_ACCESS_TOKEN with the token received after login.

## 3. Authentication APIs

### Register

Method: POST

Endpoint: /api/auth/register

Example request:

```json
{
  "full_name": "Sample Student",
  "email": "student@example.com",
  "password": "ExamplePassword123"
}