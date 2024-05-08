from sqlalchemy.orm import Session
from app import models
from app.schemas.user import CreateUser
from app.internal import security

def create_user(db: Session, user: CreateUser):
    db_user = models.User(
        userId= user.userId,
        password=security.get_password_hash(user.password),
        email= user.email,
        role= user.role,
        name= user.name
    )
    db.add(db_user)
    db.flush()
    db.refresh(db_user)
    db.commit()
    return db_user

def get_user_by_user_id(db: Session, userId: str):
    return db.query(models.User).filter(
        models.User.userId == userId
    ).first()