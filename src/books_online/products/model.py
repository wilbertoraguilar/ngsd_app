from books_online.database import Base, engine
from sqlalchemy import Column, DateTime, Integer, String, Boolean, ForeignKey, Float
from sqlalchemy.orm import Session, relationship
from books_online.auth.model import User


class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, unique=True, index=False, nullable=False)
    description = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    inventory = Column(Integer, nullable=False)


def get_product(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()


def create_product(db: Session, product: Product):
    db_product = product
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def get_all_products(db: Session) -> list[Product]:
    return db.query(Product).all()
