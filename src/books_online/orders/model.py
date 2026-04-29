from books_online.database import Base, engine
from sqlalchemy import Column, DateTime, Integer, String, Boolean, ForeignKey, Float
from sqlalchemy.orm import Session, relationship
from books_online.auth.model import User
from books_online.products.model import Product


class OrderLine(Base):
    __tablename__ = "order_line"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey("product.id"), nullable=False)
    quantity = Column(Integer, nullable=False)
    subtotal = Column(Float, nullable=False)
    order_id = Column(Integer, ForeignKey("order.id"), nullable=False)
    order = relationship("Order", back_populates="lines")


class OrderStatus(Base):
    __tablename__ = "order_status"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    status = Column(String, nullable=False)


class Order(Base):
    __tablename__ = "order"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    created_at = Column(DateTime, nullable=False)
    status_id = Column(Integer, ForeignKey("order_status.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    user = relationship("User", back_populates="orders")


User.orders = relationship("Order", order_by=Order.id, back_populates="user")
Order.lines = relationship("OrderLine", order_by=OrderLine.id, back_populates="order")


Base.metadata.create_all(engine)


def get_order(db: Session, order_id: int):
    return db.query(Order).filter(Order.id == order_id).first()


def create_order(db: Session, order: Order):
    db_order = order
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order


def create_order_line(db: Session, order_line: OrderLine):
    db_order_line = order_line
    db.add(db_order_line)
    db.commit()
    db.refresh(db_order_line)
    return db_order_line


def get_all_orders(db: Session) -> list[Order]:
    return db.query(Order).all()
