from books_online.database import SessionLocal
from books_online.products.model import Product, create_product, get_all_products, get_product

db = SessionLocal()

def get_db():
    try:
        yield db
    finally:
        db.close()

get_db()

def get_all() -> list[Product]:
    return get_all_products(db)

def get_product_by_id(product_id: int):
    return get_product(db,product_id)

def add_product(product: Product):
    return create_product(db,product)


