from sqlalchemy.orm import Session
from . import models,schemas


def get_users(db: Session):
    return db.query(models.User).all()

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_name(db: Session, name: str):
    return db.query(models.User).filter(models.User.name == name).first()

def get_user_by_name_by_password(db: Session, name: str, password: str):
    return db.query(models.User).filter(models.User.name == name).filter(models.User.password == password).first()

def create_user(db: Session, user:schemas.UserCreate):
    db_user = models.User(name = user.name, password = user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user