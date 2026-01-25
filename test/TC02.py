# test_rental_order_update_status.py

import unittest, sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from rental_order import RentalOrder

DATA_FILE = "app/data/rental_orders.txt"

class TestRentalOrderUpdateStatus(unittest.TestCase):

    def setUp(self):
        # Đảm bảo file test tồn tại và rỗng
        os.makedirs("app/data", exist_ok=True)
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            f.write("")

        # 1. Tạo rental order với status = "new"
        self.order = RentalOrder(
            order_id="O999",
            user_id="U001",
            rental_date="2025-01-01",
            return_date="2025-01-06",
            total_price="500",
            status="new"
        )
        self.order.save()

    def test_update_status_to_confirmed(self):
        # 2. Gọi update_status("confirmed")
        self.order.update_status("confirmed")

        # 3. Kiểm tra file rental_orders.txt
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()

        self.assertEqual(len(lines), 1)

        data = lines[0].strip().split("|")
        self.assertEqual(data[0], "O999")          # order_id
        self.assertEqual(data[5], "confirmed")     # status

    def tearDown(self):
        # Dọn file sau khi test
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            f.write("")

if __name__ == "__main__":
    unittest.main()
