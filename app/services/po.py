from app.services import sap_api as sap

def get_open_po(vendor_id):
    return sap.call_open_po_api(vendor_id)

def get_open_buyer():
    return sap.call_open_po__buyer_api()
