from fastapi import APIRouter, Depends , FastAPI, Request, Security, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.routers import (
    user,
    auth,
    po,
    asn
)

app = FastAPI()

origins =[
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

app.include_router(routes)