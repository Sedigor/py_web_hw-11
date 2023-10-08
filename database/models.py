from sqlalchemy import Column, Integer, String, Boolean, func
from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Contact(Base):
    
    __tablename__ = "contacts"
    
    id = Column(Integer, primary_key=True)
    first_name = Column(String(20), nullable=False)
    last_name = Column(String(30), nullable=False)
    email = Column(String, nullable=False)
    phone_number = Column(String(20), nullable=False)
    birth_date = Column(DateTime)
    additional_data = Column(String, nullable=True)
    done = Column(Boolean, default=False)
    created_at = Column('created_at', DateTime, default=func.now())

