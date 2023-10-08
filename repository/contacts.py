from typing import List
from sqlalchemy import or_
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from database.models import Contact
from schemas import ContactModel, ContactUpdate, ContactStatusUpdate


async def search_contact(sample: str, skip: int, limit: int, db: Session) -> List[Contact]:
    return db.query(Contact).filter(
        or_(
            Contact.first_name.ilike(sample),
            Contact.last_name.ilike(sample),
            Contact.email.ilike(sample)
        )
    ).offset(skip).limit(limit).all()
    

async def get_contacts_with_upcoming_birthdays(skip: int, limit: int, days: int, db: Session) -> List[Contact]:
    today = datetime.now().date()
    days_from_today = today + timedelta(days=days)

    return db.query(Contact).filter(
        (Contact.birth_date >= today) & 
        (Contact.birth_date <= days_from_today)
        ).all()


async def get_contacts(skip: int, limit: int, db: Session) -> List[Contact]:
    return db.query(Contact).offset(skip).limit(limit).all()


async def get_contact(contact_id: int, db: Session) -> Contact:
    return db.query(Contact).filter(Contact.id == contact_id).first()


async def create_contact(body: ContactModel, db: Session) -> Contact:
    contact = Contact(
        first_name = body.first_name,
        last_name = body.last_name,
        email = body.email,
        phone_number = body.phone_number,
        birth_date = body.birth_date,
        additional_data = body.additional_data
        )
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return contact


async def remove_contact(contact_id: int, db: Session) -> Contact | None:
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if contact:
        db.delete(contact)
        db.commit()
    return contact


async def update_contact(contact_id: int, body: ContactUpdate, db: Session) -> Contact | None:
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if contact:
        contact.first_name = body.first_name
        contact.last_name = body.last_name
        contact.email = body.email
        contact.phone_number = body.phone_number
        contact.birth_date = body.birth_date
        contact.additional_data = body.additional_data
        contact.done = body.done
        db.commit()
    return contact


async def update_status_contact(contact_id: int, body: ContactStatusUpdate, db: Session) -> Contact | None:
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if contact:
        contact.done = body.done
        db.commit()
    return contact