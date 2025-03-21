from typing import List

from injector import inject

from email_sender import EmailSender
from logs.logger import Logger
from orders.order_repository import OrderRepository


class OrderService:
    @inject
    def __init__(self, repository: OrderRepository, logger: Logger, email_sender: EmailSender):
        self.repository = repository
        self.logger = logger
        self.email_sender = email_sender

    def create_order(self, order_id: int, items: List[str]):
        self.logger.log(f"Створюємо замовлення {order_id} з товарами: {items}")
        success = self.repository.save_order(order_id, items)
        if success:
            self.logger.log(f"Замовлення {order_id} успішно збережено")
            self.email_sender.send_email(order_id, items)
        return success

    def fetch_order(self, order_id: int) -> dict:
        self.logger.log(f"Отримуємо замовлення {order_id}")
        order = self.repository.get_order(order_id)
        self.logger.log(f"Знайдено замовлення: {order}")
        return order
