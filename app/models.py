from sqlalchemy import Column, String, Integer
from app.database import Base, engine


class User(Base):
    __tablename__ = "user"
    id = Column(Integer(), primary_key=True)
    userId = Column(String())
    password = Column(String())


Base.metadata.create_all(bind=engine)