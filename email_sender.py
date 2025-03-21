from typing import List


class EmailSender:
    def send_email(self, order_id: int, items: List[str]):
        print(f"Лист відправлено для замовлення {order_id}: {items}")
