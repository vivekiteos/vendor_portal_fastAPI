from app.services import sap_api as sap
from app import models
from sqlalchemy.orm import Session

from app.services.common import generate_random_tracking_no

def get_asn(asn_id):
    return sap.call_get_asn_api(asn_id)

def get_all_asn(db, userId):
    return db.query(models.ASN).filter(
        models.ASN.userId == userId
    ).all()

def get_all_asn_buyer(db):
    return db.query(models.ASN).filter(
    ).all()
    
def get_asn_row(db, id):
    return db.query(models.ASN).filter(
        models.ASN.id == id
    ).first()

def get_asn_by_po_no(db, po_no, matnr):
    return db.query(models.ASN).filter(
        models.ASN.po_no == po_no,
        models.ASN.mat_code == matnr
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
    payload_data = []
    for item in PostASN.data:
        get_asn = get_asn_row(db, item.id)
        if get_asn is not None:
            payload_data.append({
                "LIFNR": userId,
                "EBELN": get_asn.po_no,
                "EBELP": get_asn.item_no,
                "MENGE": get_asn.open_qty,
                "MATNR": get_asn.mat_code,
                "EINDT": PostASN.etd,
                "NETPR": PostASN.invoice_value,
                "MENE1": item.del_qty,
                "MAKTX": get_asn.mat_desc,
                "ETA": PostASN.eta,
                "ETD": PostASN.etd
            })
    if payload_data:
        payload = {
            "INVOICE": PostASN.invoice_no,
            "DATA": payload_data
        }
        resp = sap.call_create_asn_api(payload)
        if resp['success']:
            for idx, item in enumerate(PostASN.data):  # Loop through PostASN.data again
                get_asn = get_asn_row(db, item.id)
                if get_asn is not None:
                    get_asn.status = "pending"
                    get_asn.inv_no = PostASN.invoice_no
                    get_asn.inv_value = PostASN.invoice_value
                    get_asn.asn_no = resp['field1']
                    get_asn.del_qty = item.del_qty  # Use item.del_qty from PostASN.data
                    get_asn.eta = PostASN.eta
                    get_asn.etd = PostASN.etd
                    db.commit()
                    db.refresh(get_asn)
            return True
    return False

    

def add_logistic(db: Session, logistic, userId:str):
        asn_data = db.query(models.ASN).filter(
        models.ASN.id == logistic.id
    ).first()
        if asn_data !=None:
            asn_data.tracking_Id = generate_random_tracking_no()
            asn_data.logistic_vendor =logistic.vendor_id
            asn_data.logistic_created_by= userId
            asn_data.status ="in-transit"
            db.commit()
            db.flush()
            db.refresh(asn_data)
            return 200
        
        
