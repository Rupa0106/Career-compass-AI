from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field, HttpUrl
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.models.certificate import Certificate
from app.routes.auth import get_current_user

router = APIRouter(
    prefix="/api/certificates",
    tags=["Certificates"],
)


# Request schema
class CertificateCreate(BaseModel):
    title: str = Field(min_length=2, max_length=200)
    issuer: str = Field(min_length=2, max_length=200)
    certificate_url: HttpUrl | None = None
    issue_date: str | None = Field(default=None, max_length=30)


# Response schema
class CertificateResponse(BaseModel):
    id: int
    title: str
    issuer: str
    certificate_url: str | None
    issue_date: str | None

    model_config = {"from_attributes": True}


# Add a certificate
@router.post("/", response_model=CertificateResponse)
def create_certificate(
    data: CertificateCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    certificate = Certificate(
        user_id=current_user.id,
        title=data.title,
        issuer=data.issuer,
        certificate_url=(
            str(data.certificate_url)
            if data.certificate_url
            else None
        ),
        issue_date=data.issue_date,
    )

    db.add(certificate)
    db.commit()
    db.refresh(certificate)

    return certificate


# Get all certificates of the logged-in user
@router.get("/", response_model=list[CertificateResponse])
def list_certificates(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    certificates = (
        db.query(Certificate)
        .filter(Certificate.user_id == current_user.id)
        .order_by(Certificate.id.desc())
        .all()
    )

    return certificates


# Delete a certificate
@router.delete("/{certificate_id}")
def delete_certificate(
    certificate_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    certificate = (
        db.query(Certificate)
        .filter(
            Certificate.id == certificate_id,
            Certificate.user_id == current_user.id,
        )
        .first()
    )

    if certificate is None:
        raise HTTPException(
            status_code=404,
            detail="Certificate not found.",
        )

    db.delete(certificate)
    db.commit()

    return {
        "message": "Certificate deleted successfully."
    }