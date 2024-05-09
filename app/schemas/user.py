from pydantic import BaseModel

class UserBase(BaseModel):
    userId: str
    password: str
    role: str
    email: str
    name: str

class CreateUser(UserBase):
    pass

class User(UserBase):
    id: int


class ChangePassword(BaseModel):
    current_password: str
    new_password: str