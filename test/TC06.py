# test_rental_order_save.py

import unittest, sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from rental_order import RentalOrder

DATA_FILE = "app/data/rental_orders.txt"

class TestRentalOrderSave(unittest.TestCase):

    def setUp(self):
        # Tạo thư mục và làm rỗng file trước khi test
        os.makedirs("app/data", exist_ok=True)
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            f.write("")

    def test_save_rental_order(self):
        # 1. Tạo RentalOrder object
        order = RentalOrder(
            order_id="O006",
            user_id="U001",
            rental_date="2025-01-01",
            return_date="2025-01-06",
            total_price="500",
            status="new"
        )

        # 2. Gọi save()
        order.save()

        # 3. Kiểm tra file rental_orders.txt
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()

        self.assertEqual(len(lines), 1)

        data = lines[0].strip().split("|")
        self.assertEqual(data[0], "O006")     # order_id
        self.assertEqual(data[1], "U001")     # user_id
        self.assertEqual(data[5], "new")      # status

    def tearDown(self):
        # Dọn file test
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            f.write("")

if __name__ == "__main__":
    unittest.main()
