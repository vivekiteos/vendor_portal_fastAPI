from typing import Union
from pydantic import BaseModel

class LoginBase(BaseModel):
    userId: str
    password: str

class Login(LoginBase):
    pass

class LoginResponse(BaseModel):
    token: str
    role: str
    userId: str

class Claims(BaseModel):
    sub: str
    exp: Union[int, None]
    email: Union[str, None]
    scopes: list[str]
