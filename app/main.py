from fastapi import APIRouter, Depends , FastAPI, Request, Security, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.routers import (
    user,
    auth,
    po,
    asn,
    issue,
    master
)

app = FastAPI()

origins =[
    "https://vendorportal-new.vercel.app",
    "http://182.16.16.24:8089",
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

routes = APIRouter()
auth_routes = APIRouter(dependencies=[Depends(auth.authorized_user)])

routes.include_router(
    auth.router,prefix="/auth",tags=["Auth"]
)

routes.include_router(
    user.router,prefix="/user",tags=["User"]
)

auth_routes.include_router(
    po.router,prefix="/po",tags=["PO"]
)

auth_routes.include_router(
    asn.router,prefix="/asn",tags=["ASN"]
)

auth_routes.include_router(
    issue.router,prefix="/issue",tags=["ISSUE"]
)

routes.include_router(
    master.router,prefix="/master",tags=["MASTER"]
)

app.include_router(routes)
app.include_router(auth_routes)