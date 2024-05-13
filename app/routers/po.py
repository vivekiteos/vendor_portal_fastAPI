from typing import List
from fastapi import APIRouter, Depends
from app.schemas.po import ResponseModel
from app.schemas.user import User
from app.services import po as service_po
from app.routers import auth
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.asn import get_asn_by_po_no

router = APIRouter()

@router.get("", response_model=ResponseModel)
def open_po(db: Session = Depends(get_db), current_user: User = Depends(auth.authorized_user)):
    vendor_id = current_user.userId
    po_data = service_po.get_open_po(vendor_id)
    po_items = po_data['data']
    items_to_remove: List[int] = []
    for index, item in enumerate(po_items):
        is_found = get_asn_by_po_no(db, item["ebeln"], item["matnr"])
        if is_found:
            items_to_remove.append(index)
    for index in reversed(items_to_remove):
        po_items.pop(index)

    return ResponseModel(
            success=po_data['success'],
            msg=po_data['msg'],
            openPo=str(len(po_items)),
            delQn=po_data['delQn'],
            poValue=po_data['poValue'],
            inv=po_data['inv'],
            data=po_items
        )
        

        
        
@router.get("/buyer_po")
def open_po_buyer():
    return service_po.get_open_buyer()
        
    
