import requests

LOGIN_API_URL ='http://195.234.214.189:8000/sap/bc/zsicf_vs_login?sap-client=800'
OPEN_PO_API_URL='http://195.234.214.189:8000/sap/bc/zpn97_test?sap-client=800'
GET_ASN_API_URL='http://195.234.214.189:8000/sap/bc/zsicf_vs_asnget?sap-client=800'
CREATE_ASN_API_URL='http://195.234.214.189:8000/sap/bc/zsicf_vs_asn_c?sap-client=800'

SAP_AUTH_USER_ID ='user07'
SAP_AUTH_PASS ='MSPG@0424'

def call_Login_api(userId):
    print(userId)
    auth = (SAP_AUTH_USER_ID, SAP_AUTH_PASS)
    body = {
        'form_field1': userId,
        'form_field2': '',
        'form_field3': '',
        'form_field4': ''
    }
    try:
        response = requests.post(LOGIN_API_URL, auth=auth, data=body)
        response.raise_for_status() 
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
    
def call_open_po_api(vendor_id):
    auth = (SAP_AUTH_USER_ID, SAP_AUTH_PASS)
    body = {
        'Vendor': vendor_id
    }
    try:
        response = requests.get(OPEN_PO_API_URL, auth=auth, data=body)
        response.raise_for_status() 
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
    
def call_get_asn_api(asn_id):
    auth = (SAP_AUTH_USER_ID, SAP_AUTH_PASS)
    body = {
        'form_field1': asn_id
    }
    try:
        response = requests.get(GET_ASN_API_URL, auth=auth, data=body)
        response.raise_for_status() 
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
    
def call_create_asn_api(createASN):
    auth = (SAP_AUTH_USER_ID, SAP_AUTH_PASS)
    try:
        response = requests.post(CREATE_ASN_API_URL, auth=auth, json=createASN)
        response.raise_for_status() 
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}