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


class CreateASN(BaseModel):
    data: List[Item]