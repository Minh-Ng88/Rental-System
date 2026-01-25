# test_payment_verify.py

import unittest, sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from payment import Payment

class TestPaymentVerify(unittest.TestCase):

    def test_verify_payment_paid(self):
        # 1. Tạo Payment với status = "paid"
        payment = Payment(
            payment_id="P001",
            order_id="O001",
            method="cash",
            payment_date="2025-01-06",
            status="paid"
        )

        # 2. Gọi verify_payment()
        result = payment.verify_payment()

        self.assertTrue(result)

    def test_verify_payment_not_paid(self):
        # Test thêm: status khác "paid"
        payment = Payment(
            payment_id="P002",
            order_id="O002",
            method="card",
            payment_date="2025-01-06",
            status="pending"
        )

        result = payment.verify_payment()

        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()
