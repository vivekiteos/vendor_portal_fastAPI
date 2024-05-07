from app.services import sap_api as sap
from app import models
from sqlalchemy.orm import Session

def get_asn(asn_id):
    return sap.call_get_asn_api(asn_id)

def get_all_asn(db):
    return db.query(models.ASN).filter(
    ).all()
    
def get_asn_row(db, id):
    return db.query(models.ASN).filter(
        models.ASN.id == id
    ).first()

def po_to_asn(db: Session, createASN, userId:str):
    for asn in createASN.data:
        create_asn = models.ASN(
            userId = userId,
            po_no = asn.EBELN,
            mat_code= asn.MATNR,
            mat_desc= asn.MAKTX,
            item_no = asn.EBELP,
            open_qty= asn.MENGE,
            del_qty= asn.DEL_QTY,
            price=asn.NETPR,
            status ="pending",
            plant_code = asn.plant_code,
            vendor_name= asn.vendor_name,
            vendor_code= asn.vendor_code
        )
        db.add(create_asn)
        db.flush()
        db.refresh(create_asn)
        db.commit()
    
    return 200

def save_asn(db, PostASN, userId):
    get_asn = get_asn_row(db, PostASN.id)
    if(get_asn != None):
        payload = {
            "INVOICE": PostASN.invoice_no,
            "DATA": [
                {
                    "LIFNR": userId,
                    "EBELN": get_asn.po_no,
                    "EBELP": get_asn.item_no,
                    "MENGE": get_asn.open_qty,
                    "MATNR": get_asn.mat_code,
                    "EINDT": PostASN.etd,
                    "NETPR": PostASN.invoice_value,
                    "MENE1": PostASN.del_qty,
                    "MAKTX": get_asn.mat_desc,
                    "ETA": PostASN.eta,
                    "ETD": PostASN.etd
                }
            ]
        }
        resp = sap.call_create_asn_api(payload)
        print(resp)
        if(resp['success']):
           get_asn.status= "completed"
           get_asn.inv_no = PostASN.invoice_no
           get_asn.inv_value = PostASN.invoice_value
           get_asn.asn_no = resp['field1']
           get_asn.del_qty = PostASN.del_qty
           get_asn.eta= PostASN.eta
           get_asn.etd= PostASN.etd
           db.commit()
           db.refresh(get_asn)
           return True
