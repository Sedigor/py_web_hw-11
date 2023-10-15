from typing import List

from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session

from database.db import get_db
from schemas import ContactModel, ContactResponse, ContactStatusUpdate, ContactUpdate
from repository import contacts as repository_contacts
from services.auth import Auth as auth_service
from database.models import User

router = APIRouter(prefix='/contacts', tags=["contacts"])


@router.get("/search_{sample}", response_model=List[ContactResponse])
async def search_contact(sample: str, skip: int, limit: int, db: Session = Depends(get_db)):
    contacts = await repository_contacts.search_contacts(sample, skip, limit, db)
    return contacts


@router.get("/upcoming_birthdays_for_{days}_days", response_model=List[ContactResponse])
async def search_contact(skip: int, limit: int, days: int = 7, db: Session = Depends(get_db)):
    contacts = await repository_contacts.get_contacts_with_upcoming_birthdays(skip, limit, days, db)
    return contacts


@router.get("/", response_model=List[ContactResponse])
async def read_contacts(skip: int = 0, limit: int = 20, db: Session = Depends(get_db), 
                        current_user: User = Depends(auth_service.get_current_user)):
    contacts = await repository_contacts.get_contacts(skip, limit, current_user, db)
    return contacts


@router.get("/{contact_id}", response_model=ContactResponse)
async def read_contact(contact_id: int, db: Session = Depends(get_db),
                       current_user: User = Depends(auth_service.get_current_user)):
    contact = await repository_contacts.get_contact(contact_id, current_user, db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found")
    return contact


@router.post("/", response_model=ContactResponse)
async def create_contact(body: ContactModel, db: Session = Depends(get_db),
                         current_user: User = Depends(auth_service.get_current_user)):
    return await repository_contacts.create_contact(body, current_user, db)


@router.put("/{contact_id}", response_model=ContactResponse)
async def update_Contact(body: ContactUpdate, contact_id: int, db: Session = Depends(get_db),
                         current_user: User = Depends(auth_service.get_current_user)):
    contact = await repository_contacts.update_contact(contact_id, body, current_user, db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found")
    return contact


@router.patch("/{contact_id}", response_model=ContactResponse)
async def update_status_contact(body: ContactStatusUpdate, contact_id: int, db: Session = Depends(get_db),
                                current_user: User = Depends(auth_service.get_current_user)):
    contact = await repository_contacts.update_status_contact(contact_id, body, current_user, db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found")
    return contact


@router.delete("/{contact_id}", response_model=ContactResponse)
async def remove_contact(contact_id: int, db: Session = Depends(get_db),
                         current_user: User = Depends(auth_service.get_current_user)):
    contact = await repository_contacts.remove_contact(contact_id, current_user, db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="contact not found")
    return contact

