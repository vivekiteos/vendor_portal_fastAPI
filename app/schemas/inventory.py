from typing import List
from pydantic import BaseModel

class InventoryBase(BaseModel):
    mat_code_supplier: str
    mat_code_buyer: str
    description: str
    qty: int
    uom: str

class Createinventory(BaseModel):
    data: List[InventoryBase]

class Inventory(InventoryBase):
    id: int

