from abc import ABC, abstractmethod
from typing import List

from logs.logger import Logger


class OrderRepository(ABC):
    @abstractmethod
    def save_order(self, order_id: int, items: List[str]):
        pass

    @abstractmethod
    def get_order(self, order_id: int) -> dict:
        pass


class InMemoryOrderRepository(OrderRepository):
    def __init__(self):
        self.orders = {}

    def save_order(self, order_id: int, items: List[str]):
        self.orders[order_id] = {"items": items}
        return True

    def get_order(self, order_id: int) -> dict:
        return self.orders.get(order_id, {})


class MockRepository(OrderRepository):
    def save_order(self, order_id: int, items: List[str]):
        return True

    def get_order(self, order_id: int) -> dict:
        return {"items": ["Тест"]}


# Тихий логер
class MockLogger(Logger):
    def log(self, message: str):
        pass
