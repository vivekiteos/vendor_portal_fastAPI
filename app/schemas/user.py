from pydantic import BaseModel

class UserBase(BaseModel):
    userId: str
    password: str

class CreateUser(UserBase):
    pass

class User(UserBase):
    id: int