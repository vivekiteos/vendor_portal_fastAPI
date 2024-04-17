from sqlalchemy import Column, String, Integer, Date, func
from app.database import Base, engine


class User(Base):
    __tablename__ = "user"
    id = Column(Integer(), primary_key=True)
    userId = Column(String())
    password = Column(String())


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
    created_date = Column(Date(), default=func.now())


Base.metadata.create_all(bind=engine)