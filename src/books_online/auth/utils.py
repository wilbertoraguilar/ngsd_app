from books_online.auth.model import User, get_token_by_token
from books_online.database import SessionLocal
import datetime

db = SessionLocal()

def get_db():
    try:
        yield db
    finally:
        db.close()

get_db()

def get_token_user(token: str):
    db_token = get_token_by_token(db,token[7:])
    if db_token:
        return {"user": db_token.user}
    return None

def is_token_valid(token: str) -> bool:
    db_token = get_token_by_token(db,token[7:])
    if  db_token and db_token.valid_until > datetime.datetime.now(): # type: ignore
         return True
    return False

def is_token_user_admin(token: str) -> bool:
    db_token = get_token_by_token(db,token[7:])
    if  db_token and db_token.user.admin:
         return True
    return False

def get_db_token(token: str):
    return get_token_by_token(db,token[7:])
