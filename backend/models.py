from operator import index
from sqlalchemy import Boolean,Column,ForeignKey,Integer,String,Float
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    password = Column(String)
    is_active = Column(Boolean, default=True)

class Sales(Base):
    __tablename__ = "sales"

    year = Column(Integer, primary_key=True, index=True)
    department = Column(String, primary_key=True, index=True)
    sales = Column(float)