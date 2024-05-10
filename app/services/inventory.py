from sqlalchemy import func
from sqlalchemy.orm import Session
from app import models
from app.schemas.inventory import Createinventory
from app.internal import security
from datetime import date

def create_inv(db: Session, inventories: Createinventory, userId):
    for inv in inventories.data:
        print(inv)
        db_inv = models.Inventory(
            userId=userId,
            mat_code_supplier=inv.mat_code_supplier,
            mat_code_customer=inv.mat_code_customer,
            description=inv.description,
            qty=inv.qty,
            uom=inv.uom
        )
        db.add(db_inv)
        db.flush()
        db.refresh(db_inv)
        db.commit()
    return "Inventory items created successfully"

def get_inv_vendor(db: Session, userId: str):
    current_date = date.today()
    return db.query(models.Inventory).filter(
        models.Inventory.userId == userId,
        func.DATE(models.Inventory.created_date) == current_date
    ).all()
