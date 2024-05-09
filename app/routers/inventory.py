from app.database import get_db
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.routers import auth
from app.schemas.inventory import Inventory, Createinventory
from app.schemas.user import User
from app.services import inventory as service_inventory

router = APIRouter()

@router.post("")
def create_inventory(Createinventory: Createinventory, db: Session = Depends(get_db), current_user: User = Depends(auth.authorized_user)):
    return service_inventory.create_inv(db, Createinventory, current_user.userId)


@router.get("")
def get_inv(db: Session = Depends(get_db), current_user: User = Depends(auth.authorized_user)):
    if current_user.role.lower() =="vendor":
        vendor_id =current_user.userId
        return service_inventory.get_inv_vendor(db, vendor_id)
    else:
        return None


