import os
from pathlib import Path
from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parents[3]

# Load environment variables from the project root .env file
load_dotenv(PROJECT_ROOT / ".env")

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    f"sqlite:///{(PROJECT_ROOT / 'career_compass.db').as_posix()}"
)

JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "")
JWT_ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

FRONTEND_ORIGINS = [
    "http://127.0.0.1:8000",
    "http://localhost:8000",
]
GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID", "")