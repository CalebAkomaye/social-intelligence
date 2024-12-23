from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr
    username: str

class UserCreate(UserBase):
        password: str

class Token(BaseModel):
    access_token: str
    token_type: str

