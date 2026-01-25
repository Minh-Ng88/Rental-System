# test_admin_generate_report.py

import unittest, sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from admin import Admin

ORDER_FILE = "app/data/rental_orders.txt"
PAYMENT_FILE = "app/data/payments.txt"

class TestAdminGenerateReport(unittest.TestCase):

    def setUp(self):
        # Tạo thư mục dữ liệu
        os.makedirs("app/data", exist_ok=True)

        # Tạo dữ liệu rental_orders.txt (2 orders)
        with open(ORDER_FILE, "w", encoding="utf-8") as f:
            f.write(
                "O01|U01|2025-01-01|2025-01-06|500|new\n"
                "O02|U02|2025-01-02|2025-01-07|600|confirmed\n"
            )

        # Tạo dữ liệu payments.txt (3 payments)
        with open(PAYMENT_FILE, "w", encoding="utf-8") as f:
            f.write(
                "P01|O01|cash|2025-01-01|paid\n"
                "P02|O02|card|2025-01-02|paid\n"
                "P03|O02|cash|2025-01-03|pending\n"
            )

        # Tạo Admin object
        self.admin = Admin(
            user_id="A01",
            full_name="Admin User",
            email="admin@gmail.com",
            password="admin123",
            phone="0900000000",
            address="Admin Address",
            created_at="2025-01-01",
            role="admin"
        )

    def test_generate_report(self):
        # 1. Admin gọi generate_report()
        report = self.admin.generate_report()

        # 2. Kiểm tra kết quả
        self.assertEqual(report["total_orders"], 2)
        self.assertEqual(report["total_payments"], 3)

    def tearDown(self):
        # Dọn file test
        with open(ORDER_FILE, "w", encoding="utf-8") as f:
            f.write("")
        with open(PAYMENT_FILE, "w", encoding="utf-8") as f:
            f.write("")

if __name__ == "__main__":
    unittest.main()
