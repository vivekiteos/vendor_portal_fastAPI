import time
from sqlalchemy.orm import Session
from app import models
from app.schemas.auth import Claims, Login
from app.internal import security
from app.schemas.user import User
from app.services import sap_api as sap
from app.services import user as service_users
from app.config import settings


def create_access_token(user: User, scopes: list[str]):
    exp= int(time.time() + settings.JWT_EXPIRY_MINUTES * 60)
    return security.create_token(
        Claims(
            sub=str(user.userId), email="",exp=exp,scopes=scopes
        ).model_dump()
    )


def authenticate(db: Session, username: str, password: str):
    user = get_user(db,username)
    if user:
        if security.verify_password(password, user.password):
            return sap.call_Login_api(username)

def get_user_by_pass(db, login):
    return db.query(models.User).filter(
        models.User.userId == login.userId,
        models.User.password == login.password
    ).first()


def get_user(db, userId):
    return db.query(models.User).filter(
        models.User.userId == userId
    ).first()
