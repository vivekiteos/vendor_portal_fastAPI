from app.database import get_db
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.internal import security

from app.routers import auth
from app.schemas.user import ChangePassword, User,UserBase, CreateUser
from app.services import user as service_users

router = APIRouter()

@router.post("", response_model=User)
def create_user(user: CreateUser, db: Session = Depends(get_db)):
    db_user = service_users.get_user_by_user_id(db, user.userId)
    if db_user:
        raise HTTPException(status_code=400, detail="user already exists")
    return service_users.create_user(db, user)


@router.post("/change_password", response_model=User)
def change_password(user: ChangePassword, db: Session = Depends(get_db), current_user: User = Depends(auth.authorized_user)):
    db_user = service_users.get_user_by_user_id(db, current_user.userId)
    if security.verify_password(user.current_password, db_user.password):
        return service_users.update_password(db, db_user, user.new_password)
    
