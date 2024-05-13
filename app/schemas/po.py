from typing import List, Optional
from pydantic import BaseModel

class DataItem(BaseModel):
    lifnr: str
    ebeln: str
    ebelp: int
    menge: float
    matnr: str
    netpr: float
    bpumz: int
    eindt: str
    eketQty: float
    maktx: str
    unitkey: str
    unittxt: str
    werks: str
    vendorName: str

class ResponseModel(BaseModel):
    success: bool
    msg: str
    openPo: str
    poValue: str
    delQn: str
    inv: str
    data: List[DataItem]
