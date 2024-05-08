from typing import List
from pydantic import BaseModel

class ASNBase(BaseModel):
    pass

class Item(BaseModel):
    EBELN: str
    EBELP: int
    MENGE: int
    MATNR: str
    EINDT: str
    NETPR: int
    MENE1: int
    MAKTX: str
    DEL_QTY: str
    plant_code: str
    vendor_code: str
    vendor_name: str
    


class CreateASN(BaseModel):
    data: List[Item]


class ASNItem(BaseModel):
    LIFNR: str
    EBELN: str
    EBELP: int
    MENGE: int
    MATNR: str
    EINDT: str
    NETPR: int
    MENE1: int
    MAKTX: str
    ETA: str
    ETD: str

class SubmitASN(BaseModel):
    invoice: str
    data: List[ASNItem]

class PostASN(BaseModel):
    invoice_no: str
    invoice_value: str
    id: int
    eta: str
    etd: str
    del_qty: str


class AddLogistics(BaseModel):
    id: str
    vendor_id: str