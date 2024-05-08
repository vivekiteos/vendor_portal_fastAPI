from sqlalchemy import Column, String, Integer, Date, func
from app.database import Base, engine


class User(Base):
    __tablename__ = "user"
    id = Column(Integer(), primary_key=True)
    userId = Column(String())
    password = Column(String())
    role = Column(String())
    email = Column(String())
    name = Column(String())
    created_date = Column(Date(), default=func.now())



class ASN(Base):
    __tablename__ = "asn"
    id = Column(Integer(), primary_key=True)
    userId = Column(String())
    po_no = Column(String())
    mat_code = Column(String())
    mat_desc = Column(String())
    item_no = Column(String())
    open_qty = Column(String())
    del_qty = Column(String())
    price = Column(String())
    inv_no = Column(String())
    inv_value = Column(String())
    asn_no = Column(String())
    status = Column(String())
    eta = Column(String())
    etd = Column(String())
    plant_code = Column(String())
    vendor_name = Column(String())
    vendor_code = Column(String())
    tracking_Id = Column(String())
    logistic_vendor = Column(String())
    logistic_created_by = Column(String())
    created_date = Column(Date(), default=func.now())

class Issue(Base):
    __tablename__ = "issue"
    id = Column(Integer(), primary_key=True)
    issue_no= Column(String())
    userId = Column(String())
    supplier= Column(String())
    complaint_ref= Column(String())
    priority= Column(String())
    material= Column(String())
    issue_date= Column(Date())
    ref_grn_po= Column(String())
    action_date= Column(Date())
    issue_title= Column(String())
    issue_desc= Column(String())
    submit_type=Column(String())
    status=Column(String())
    created_date = Column(Date(), default=func.now())


class IssueComments(Base):
    __tablename__ = "issue_comments"
    id = Column(Integer(), primary_key=True)
    userId = Column(String())
    issueId = Column(Integer())
    comments = Column(String())
    created_date = Column(Date(), default=func.now())


Base.metadata.create_all(bind=engine)