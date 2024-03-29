from sqlalchemy.orm import Session
from app import models
from app.schemas.auth import Login
from app.services import sap_api as sap

def user_login(db: Session, login: Login):
    is_valid_user = get_user_by_pass(db,login)
    if is_valid_user:
        return sap.call_Login_api(login.userId)

def get_user_by_pass(db, login):
    return db.query(models.User).filter(
        models.User.userId == login.userId,
        models.User.password == login.password
    ).first()
