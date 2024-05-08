from fastapi import APIRouter

router = APIRouter()

@router.get("/suppliers")
def get_suppliers():
    suppliers = [
        {"id": "1", "name": "Supplier 1"},
        {"id": "2", "name": "Supplier 2"},
        {"id": "3", "name": "Supplier 3"}
    ]
    return suppliers


@router.get("/materials")
def get_materials():
    materials = [
        {"id": "1", "name": "Material 1"},
        {"id": "2", "name": "Material 2"},
        {"id": "3", "name": "Material 3"}
    ]
    return materials


@router.get("/ref_grn_no")
def ref_grn_no():
    ref_grn_no = [
        {"id": "1", "name": "REF 1"},
        {"id": "2", "name": "REF 2"},
        {"id": "3", "name": "REF 3"}
    ]
    return ref_grn_no

@router.get("/vendor")
def vendor():
    vendor = [
        {"id": "1", "name": "vendor 1"},
        {"id": "2", "name": "vendor 2"},
        {"id": "3", "name": "vendor 3"}
    ]
    return vendor