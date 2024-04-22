from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.asn import CreateASN
from app.services import asn as service_asn

router = APIRouter()

@router.get("")
def get_asn(asn_id: str):
    return service_asn.get_asn(asn_id)


@router.post("")
def create_asn(createASN: CreateASN, db: Session = Depends(get_db)):
    return service_asn.create_asn(createASN)

@router.post("")
def po_to_asn(createASN: CreateASN, db: Session = Depends(get_db)):
    return service_asn.create_asn(createASN)
    
