import time
from typing import Annotated
from app.database import get_db
from fastapi import APIRouter, Depends,Form,status,Request, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import(
    OAuth2PasswordRequestForm,
    OAuth2PasswordBearer,
    SecurityScopes,
)

from app.schemas.auth import Login, LoginResponse
from app.schemas.user import User
from app.services import auth as service_auth, user as service_users
from app.services.opa import OpaInput

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl= "auth",
    scopes={
        "me":"Read and write access to user's data"
    },
)

def raise_authentication_exception(required_scopes, detail):
    www_authenticate = (
        f"Bearer scope={required_scopes.scope_str}"
        if required_scopes.scopes
        else "Bearer"
    )
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=detail,
        headers={"WWW-Authenticate": www_authenticate},
    )


def authorized_user(
    req: Request,
    required_scopes: SecurityScopes,
    token: Annotated[str, Depends(oauth2_scheme)],
    db: Session = Depends(get_db),
) -> User:
    try:
        claims = auth.decode_access_token(token)
    except Exception as e:
        raise_authentication_exception(
            required_scopes, detail=f"JWT error: {e}"
        )
    if claims.exp < int(time.time()):
        raise_authentication_exception(
            required_scopes, detail="Token expired."
        )
    if not all(scope in claims.scopes for scope in required_scopes.scopes):
        raise_authentication_exception(
            required_scopes, detail="Not enough permissions (scope)."
        )
    user = service_users.get_user_by_user_id(db, user_id=claims.sub)
    if not user:
        raise_authentication_exception(
            required_scopes, detail="Could not validate credentials."
        )
    if not auth.opa_check(
        OpaInput(
            method=req.method, path=req.url.path.split("/")[1:], claims=claims
        )
    ):
        raise_authentication_exception(
            required_scopes, detail="Not enough permissions (policy)."
        )
    return user

@router.post("")
def auth(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session = Depends(get_db)) -> LoginResponse:
    db_user = service_users.get_user_by_user_id(db, form_data.username)
    if db_user is None:
        raise HTTPException(status_code=400, detail="invalid user")
    response = service_auth.authenticate(db, form_data.username, form_data.password)
    if response:
        return LoginResponse(
            token= service_auth.create_access_token(db_user, form_data.scopes),
            role=response['data'][0]['role'],
            userId=response['data'][0]['id'],
            name=response['data'][0]['name'],
            city=response['data'][0]['city']
        )
    
