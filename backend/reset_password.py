from app.database.connection import SessionLocal
from app.models.user import User
from app.core.security import get_password_hash

email = "rupasri14@gmail.com"

db = SessionLocal()

try:
    user = db.query(User).filter(User.email == email).first()

    if user:
        new_password = input("Enter a new password: ")
        user.hashed_password = get_password_hash(new_password)
        db.commit()
        print("Password reset successful!")
    else:
        print("User not found!")

finally:
    db.close()