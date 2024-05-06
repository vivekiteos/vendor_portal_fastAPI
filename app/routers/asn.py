from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.asn import CreateASN, PostASN, SubmitASN
from app.services import asn as service_asn


router = APIRouter()

@router.get("/get_asn_by_id")
def get_asn_by_id(asn_id: str):
    return service_asn.get_asn(asn_id)

@router.get("/get_asn")
def get_asn(db: Session = Depends(get_db)):
    return service_asn.get_all_asn(db)


@router.post("/submit_asn")
def submit_asn(PostASN: PostASN, db: Session = Depends(get_db)):
    userId="0000100005"
    return service_asn.save_asn(db, PostASN, userId)

@router.post("/po_to_asn")
def po_to_asn(createASN: CreateASN, db: Session = Depends(get_db)):
    userId="0000100005"
    return service_asn.po_to_asn(db, createASN, userId)
    
