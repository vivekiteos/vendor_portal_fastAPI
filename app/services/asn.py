from app.services import sap_api as sap

def get_asn(asn_id):
    return sap.call_get_asn_api(asn_id)


def create_asn(createASN):
    return sap.call_create_asn_api(createASN)