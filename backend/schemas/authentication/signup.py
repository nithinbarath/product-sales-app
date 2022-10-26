from pydantic import BaseModel
from typing import Optional




class Signup(BaseModel):
    username:str
    email: str
    password: str

class Login(BaseModel):
    email: str
    password: str


class RefreshTokenSchema(BaseModel):
    access_token: str
    token_type: Optional[str] = "bearer"