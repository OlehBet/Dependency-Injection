import os

from injector import Module, singleton

from email_sender import EmailSender
from logs.logger import ConsoleLogger, FileLogger
from logs.logger import Logger
from orders.order_repository import InMemoryOrderRepository, OrderRepository


class AppModule(Module):
    def configure(self, binder):
        if os.getenv("USE_FILE_LOGGER") == "true":
            binder.bind(Logger, to=FileLogger, scope=singleton)
        else:
            binder.bind(Logger, to=ConsoleLogger, scope=singleton)

        binder.bind(OrderRepository, to=InMemoryOrderRepository, scope=singleton)
        binder.bind(EmailSender, to=EmailSender, scope=singleton)
