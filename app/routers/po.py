from fastapi import APIRouter, Depends
from app.schemas.user import User
from app.services import po as service_po
from app.routers import auth

router = APIRouter()

@router.get("")
def open_po(current_user: User = Depends(auth.authorized_user)):
    if current_user.role.lower() =="vendor":
        vendor_id =current_user.userId
        return service_po.get_open_po(vendor_id)
    else:
        return service_po.get_open_buyer()

    
