import time
from model.order import Order
from service.crud_service import CrudService
from db.order_db import order_db


class OrderService(CrudService):
    def get(self, name: str):
        for order in order_db:
            if order.name == name:
                return order
        print(f"Order with name{name} not found")

    def persist(self, order: Order):
        order_db.append(order)

    def delete(self, order: Order):
        order_db.remove(order)

    def update(self, id, order: Order):
        order_to_update: Order = None
        order_index: int = None

        for index, o in enumerate(order_db):
            if o.id == id:
                order_to_update = o
                order_index = index

        if order_to_update is None:
            print(f"Order with id: {id} not found")
            return

        order_to_update.username = order.name
        order_to_update.password = order.date
        order_to_update.update_date = time.ctime(time.time())

        order_db[order_index] = order_to_update
