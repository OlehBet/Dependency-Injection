import os

from injector import Injector

from app_module import AppModule
from email_sender import EmailSender
from logs.logger import ConsoleLogger
from orders.order_repository import InMemoryOrderRepository, MockRepository, MockLogger
from orders.order_service import OrderService


def main():
    os.environ["USE_FILE_LOGGER"] = "true"

    injector = Injector([AppModule()])
    order_service = injector.get(OrderService)

    print("\nСтворення замовлень через DI:")
    order_service.create_order(1, ["Книга", "Ручка"])
    order_service.create_order(2, ["Ноутбук"])

    order = order_service.fetch_order(1)
    print(f"Отримано замовлення: {order}")

    # Вручну
    print("\nСтворення замовлення вручну:")
    email_sender = EmailSender()
    logger = ConsoleLogger()
    repository = InMemoryOrderRepository()
    manual_order_service = OrderService(repository, logger, email_sender)

    manual_order_service.create_order(3, ["Тестовий товар"])
    order = manual_order_service.fetch_order(3)
    print(f"Отримано замовлення: {order}")

    # Mock
    print("\nТестування без DI:")
    mock_repository = MockRepository()
    mock_logger = MockLogger()

    mock_order_service = OrderService(mock_repository, mock_logger, email_sender)

    success = mock_order_service.create_order(1, ["Тестовий товар"])
    print(f"Створено замовлення: {success}")

    order = mock_order_service.fetch_order(1)
    print(f"Отримано замовлення: {order}")


if __name__ == "__main__":
    main()
