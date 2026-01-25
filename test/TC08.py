# test_payment_is_paid.py

import unittest, sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from payment import Payment

DATA_FILE = "app/data/payments.txt"

class TestPaymentIsPaid(unittest.TestCase):

    def setUp(self):
        # Tạo thư mục và file dữ liệu test
        os.makedirs("app/data", exist_ok=True)

        with open(DATA_FILE, "w", encoding="utf-8") as f:
            f.write(
                "P001|101|cash|2025-01-06|paid\n"
                "P002|102|card|2025-01-06|pending\n"
            )

    def test_is_paid_true(self):
        # Gọi is_paid với order_id có status = paid
        result = Payment.is_paid("101")
        self.assertTrue(result)

    def test_is_paid_false(self):
        # Gọi is_paid với order_id chưa paid
        result = Payment.is_paid("102")
        self.assertFalse(result)

    def tearDown(self):
        # Dọn file sau khi test
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            f.write("")

if __name__ == "__main__":
    unittest.main()
