from datetime import datetime
from typing import Optional as TypingOptional
from pydantic import BaseModel, EmailStr, Field


class ContactBase(BaseModel):
    first_name: str = Field(max_length=20)
    last_name: str = Field(max_length=30)
    email: EmailStr
    phone_number: str = Field(max_length=20)
    
class ContactModel(ContactBase):
    birth_date: TypingOptional[datetime]
    additional_data: TypingOptional[str]

class ContactUpdate(ContactModel):
    done: bool

class ContactStatusUpdate(BaseModel):
    done: bool
    
class ContactResponse(ContactModel):
    id: int
    created_at: datetime
    
    class Config:
        orm_mode = True


class UserModel(BaseModel):
    username: str = Field(min_length=5, max_length=16)
    email: str
    password: str = Field(min_length=6, max_length=10)


class UserDb(BaseModel):
    id: int
    username: str
    email: str
    created_at: datetime
    avatar: str

    class Config:
        orm_mode = True


class UserResponse(BaseModel):
    user: UserDb
    detail: str = "User successfully created"


class TokenModel(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"

