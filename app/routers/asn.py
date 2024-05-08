from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.routers import auth
from app.schemas.asn import AddLogistics, CreateASN, PostASN, SubmitASN
from app.schemas.user import User
from app.services import asn as service_asn


router = APIRouter()

@router.get("/get_asn_by_id")
def get_asn_by_id(asn_id: str):
    return service_asn.get_asn(asn_id)

@router.get("/get_asn")
def get_asn(db: Session = Depends(get_db), current_user: User = Depends(auth.authorized_user)):
    if current_user.role.lower() =="vendor":
        userId= current_user.userId
        return service_asn.get_all_asn(db, userId)
    else:
        return service_asn.get_all_asn_buyer(db) 


@router.post("/submit_asn")
def submit_asn(PostASN: PostASN, db: Session = Depends(get_db), current_user: User = Depends(auth.authorized_user)):
    userId= current_user.userId
    return service_asn.save_asn(db, PostASN, userId)

@router.post("/po_to_asn")
def po_to_asn(createASN: CreateASN, db: Session = Depends(get_db), current_user: User = Depends(auth.authorized_user)):
    userId= current_user.userId
    return service_asn.po_to_asn(db, createASN, userId)

@router.post("/add_logistic")
def add_logistic(AddLogistics: AddLogistics, db: Session = Depends(get_db), current_user: User = Depends(auth.authorized_user)):
    userId= current_user.userId
    return service_asn.add_logistic(db, AddLogistics, userId)
    
