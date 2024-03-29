from app.database import get_db
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas.auth import Login, LoginResponse
from app.services import auth as service_auth, user as service_users

router = APIRouter()

@router.post("", response_model=LoginResponse)
def auth(login: Login, db: Session = Depends(get_db)):
    db_user = service_users.get_user_by_user_id(db, login.userId)
    if db_user is None:
        raise HTTPException(status_code=400, detail="invalid user")
    response = service_auth.user_login(db, login)
    return LoginResponse(
        token="",
        role=response['data'][0]['role'],
        userId=response['data'][0]['id']
    )
