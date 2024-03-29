from app.database import get_db
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas.user import User,UserBase, CreateUser
from app.services import user as service_users

router = APIRouter()

@router.post("", response_model=User)
def create_user(user: CreateUser, db: Session = Depends(get_db)):
    db_user = service_users.get_user_by_user_id(db, user.userId)
    if db_user:
        raise HTTPException(status_code=400, detail="user already exists")
    return service_users.create_user(db, user)
