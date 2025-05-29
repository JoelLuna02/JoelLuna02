"""Declaración de modelos"""
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.dialects.postgresql import TEXT, ARRAY
from sqlalchemy.sql import func

from database.config import Base

class User(Base):
    """Modelo de usuario"""
    __tablename__ = "portfolio_user"

    user_id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    about_me = Column(TEXT(500), nullable=True)
    job_titles = Column(ARRAY(String(60)), nullable=False)
    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    password = Column(String(100), nullable=False)
    created_at = Column(DateTime, nullable=False, server_default=func.now())
    updated_at = Column(DateTime, nullable=False, onupdate=func.now())

    def __repr__(self):
        return f"<User(id={self.user_id}, username={self.username}, email={self.email})>"

