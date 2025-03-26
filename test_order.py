import unittest
from unittest.mock import MagicMock
from email_sender import EmailSender
from logs.logger import ConsoleLogger
from orders.order_repository import InMemoryOrderRepository
from orders.order_service import OrderService


class TestInMemoryOrderRepository(unittest.TestCase):
    def setUp(self):
        self.repository = InMemoryOrderRepository()

    def test_save_order(self):
        result = self.repository.save_order(1, ["Книга", "Ручка"])
        self.assertTrue(result)
        self.assertEqual(self.repository.get_order(1), {"items": ["Книга", "Ручка"]})

    def test_get_order_not_found(self):
        self.assertEqual(self.repository.get_order(99), {})

class TestConsoleLogger(unittest.TestCase):
    def test_log(self):
        logger = ConsoleLogger()
        with unittest.mock.patch('builtins.print') as mock_print:
            logger.log("Test message")
            mock_print.assert_called_with("[INFO] Test message")

class TestOrderService(unittest.TestCase):
    def setUp(self):
        self.mock_repo = MagicMock()
        self.mock_logger = MagicMock()
        self.mock_email_sender = MagicMock()
        self.service = OrderService(self.mock_repo, self.mock_logger, self.mock_email_sender)

    def test_create_order(self):
        self.mock_repo.save_order.return_value = True
        self.service.create_order(1, ["Книга", "Ручка"])
        self.mock_repo.save_order.assert_called_once_with(1, ["Книга", "Ручка"])
        self.mock_logger.log.assert_called()
        self.mock_email_sender.send_email.assert_called_once_with(1, ["Книга", "Ручка"])

    def test_fetch_order(self):
        self.mock_repo.get_order.return_value = {"items": ["Книга"]}
        order = self.service.fetch_order(1)
        self.assertEqual(order, {"items": ["Книга"]})
        self.mock_logger.log.assert_called()

if __name__ == "__main__":
    unittest.main()
