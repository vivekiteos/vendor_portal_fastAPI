from fastapi import APIRouter
from app.services import po as service_po

router = APIRouter()

@router.get("")
def open_po():
    vendor_id ='0000100005'
    return service_po.get_open_po(vendor_id)
