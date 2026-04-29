from books_online.database import SessionLocal
from books_online.orders.model import Order, OrderStatus


db = SessionLocal()


def get_db():
    try:
        yield db
    finally:
        db.close()


get_db()


def get_all_orders():
    return db.query(Order).order_by("id").all()


def get_orders_by_user_id(user_id: int):
    return db.query(Order).filter_by(user_id=user_id).all()


def get_order_by_id(order_id: int):
    return db.query(Order).filter_by(id=order_id).first()


def create_new_order(order: Order):
    db.add(order)
    db.commit()
    db.refresh(order)
    return order


def create_order_line(order_line):
    db.add(order_line)
    db.commit()
    db.refresh(order_line)
    return order_line


def get_first_status():
    return db.query(OrderStatus).order_by(OrderStatus.id).first()


def update_order_status(order_id: int):
    order = db.query(Order).filter_by(id=order_id).first()
    if order:
        status_list = db.query(OrderStatus).order_by(OrderStatus.id).all()
        is_last = False
        for status in status_list:
            if is_last:
                order.status_id = status.id
                break
            if status.id == order.status_id:  # type: ignore
                is_last = True
        db.commit()
        return True
    return False

def remove_order(order_id: int):
    order = db.query(Order).filter_by(id=order_id).first()
    if order:
        db.delete(order)
        db.commit()
