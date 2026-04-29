from datetime import datetime, timedelta
from uuid import uuid4

from sqlalchemy import Column, DateTime, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import Session, relationship
from books_online.database import Base, engine


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, unique=True, index=False, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    admin = Column(Boolean, default=True)
    orders = relationship("Order", back_populates="user")


class Token(Base):
    __tablename__ = "token"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    token = Column(String, unique=True, index=True, nullable=False)
    valid_until = Column(DateTime, nullable=False)
    user = relationship("User", back_populates="tokens")


User.tokens = relationship("Token", order_by=Token.id, back_populates="user")
Base.metadata.create_all(engine)


def get_user(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def create_user(db: Session, user: User):
    try:
        db_user = user
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    except Exception as e:
        db.rollback()
        return None



def get_token(db: Session, user_id: Integer) -> Token:
    token = (
        db.query(Token)
        .filter(Token.user_id == user_id)
        .filter(Token.valid_until > datetime.now())
        .first()
    )
    if token:
        return token
    else:
        token_str = str(uuid4())
        valid_until = datetime.now() + timedelta(days=1)
        token = Token(user_id=user_id, token=token_str, valid_until=valid_until)
        db.add(token)
        db.commit()
        db.refresh(token)
        return token


def get_token_by_token(db: Session, token_str: str) -> Token:
    return (
        db.query(Token)
        .filter(Token.token == token_str)
        .filter(Token.valid_until > datetime.now())
        .first()
    )


def check_token(db: Session, token: str):
    pass
