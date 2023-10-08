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


