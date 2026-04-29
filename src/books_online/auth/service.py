import bcrypt
from uuid import uuid4
from books_online.auth.model import create_user, get_user, get_token, User, Token
from books_online.database import SessionLocal

db = SessionLocal()


def get_db():
    try:
        yield db
    finally:
        db.close()


get_db()


def login(email: str, password: str) -> str | None:
    user = get_user(db, email)
    if not user:
        return None
    hash = user.password_hash.encode("utf-8")  # type: ignore
    if bcrypt.checkpw(password.encode("utf-8"), hash):
        token = get_token(db, user.id)  # type: ignore
        return str(token.token)
    return None


def register(name: str, email: str, password: str, admin: bool = False) -> User:
    password_hash = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    user = User(
        name=name, email=email, password_hash=password_hash.decode("utf-8"), admin=admin
    )
    return create_user(db, user)
