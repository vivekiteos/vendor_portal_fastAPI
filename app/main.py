from fastapi import APIRouter, Depends , FastAPI, Request, Security, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.routers import (
    user,
    auth,
    po,
    asn,
    issue
)

app = FastAPI()

origins =[
    "http://182.16.16.24:8089"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

routes = APIRouter()

routes.include_router(
    auth.router,prefix="/auth",tags=["Auth"]
)

routes.include_router(
    user.router,prefix="/user",tags=["User"]
)

routes.include_router(
    po.router,prefix="/po",tags=["PO"]
)

routes.include_router(
    asn.router,prefix="/asn",tags=["ASN"]
)

routes.include_router(
    issue.router,prefix="/issue",tags=["ISSUE"]
)

app.include_router(routes)