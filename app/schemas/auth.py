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
