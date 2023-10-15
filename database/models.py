from sqlalchemy import Column, Integer, String, Boolean, func
from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey

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
    user_id = Column('user_id', ForeignKey('users.id', ondelete='CASCADE'), default=None)
    user = relationship('User', backref="contacts")
    
    
class User(Base):
        
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    username = Column(String(50))
    email = Column(String(250), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    created_at = Column('crated_at', DateTime, default=func.now())
    avatar = Column(String(255), nullable=True)
    refresh_token = Column(String(255), nullable=True)

