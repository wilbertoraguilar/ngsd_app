

# from celery import Celery

from books_online.orders.model import Order, OrderLine
from books_online.orders.service import create_order_line


# celery_app = Celery('tasks', broker='amqp://admin:admin@localhost:5672/bo_vhost', backend='redis://:admin@localhost:6379/0')
# celery_app.conf.broker_transport_options = {
#     'visibility_timeout': 3600,
#     'max_connections': 10,
#     'socket_timeout': 5,
#     'retry_on_timeout': True
# }

# @celery_app.task
def process_basket(order: Order,basket: list):
    for item in basket:
        product = get_product_by_id(item.get("product_id")) # type: ignore
        if not product:
            return {"error": "Product not found"}
        quantity = item.get("quantity")

        if product.inventory < quantity: # type: ignore
            return {"error": "Not enough inventory"}
        product.inventory -= quantity # type: ignore
        order_line = OrderLine(product_id=product.id, quantity=quantity, subtotal=product.price * quantity, order_id=order.id)
        new_order_line = create_order_line(order_line)
        print("Order Line created: ", new_order_line )
        update_product_inventory(product.id, quantity) # type: ignore
