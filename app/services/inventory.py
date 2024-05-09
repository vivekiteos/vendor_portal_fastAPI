from sqlalchemy import func
from sqlalchemy.orm import Session
from app import models
from app.schemas.inventory import Createinventory
from app.internal import security

def create_inv(db: Session, inventory: Createinventory, userId):
    db_inv = models.Inventory(
        userId= userId,
        mat_code_supplier= inventory.mat_code_supplier,
        mat_code_buyer= inventory.mat_code_buyer,
        description= inventory.description,
        qty=inventory.qty,
        uom=inventory.uom
    )
    db.add(db_inv)
    db.flush()
    db.refresh(db_inv)
    db.commit()
    return db_inv

def get_inv_vendor(db: Session, userId: str):
    return db.query(models.User).filter(
        models.Inventory.userId == userId,
        models.Inventory.created_date == func.now()
    ).all()
