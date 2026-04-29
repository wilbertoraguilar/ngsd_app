from celery import Celery
import os
from books_online.orders.model import OrderLine
from books_online.orders.service import create_order_line
from books_online.products.service import get_product_by_id, update_product_inventory


celery_app = Celery(
    "tasks",
    broker=os.getenv("CELERY_BROKER_URL"),
    backend=os.getenv("CELERY_BACKEND_URL"),
)


@celery_app.task
def process_basket(order_id: int, basket: list):
    for item in basket:
        product = get_product_by_id(item.get("product_id"))  # type: ignore
        if not product:
            return {"error": "Product not found"}
        quantity = item.get("quantity")

        if product.inventory < quantity:  # type: ignore
            return {"error": "Not enough inventory"}
        product.inventory -= quantity  # type: ignore
        order_line = OrderLine(
            product_id=product.id,
            quantity=quantity,
            subtotal=product.price * quantity,
            order_id=order_id,
        )
        new_order_line = create_order_line(order_line)
        print("Order Line created: ", new_order_line)
        update_product_inventory(product.id, quantity)  # type: ignore
