# test_staff_create_contract.py

import unittest, sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from staff import Staff

DATA_FILE = "app/data/contracts.txt"

class TestStaffCreateContract(unittest.TestCase):

    def setUp(self):
        # Tạo thư mục và file dữ liệu test
        os.makedirs("app/data", exist_ok=True)

        # Làm rỗng file contracts.txt
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            f.write("")

        # Tạo Staff object
        self.staff = Staff(
            user_id="S001",
            full_name="Tran Van Staff",
            email="staff@gmail.com",
            password="staff123",
            phone="0900000011",
            address="Staff Address",
            created_at="2025-01-01",
            role="staff"
        )

    def test_create_contract(self):
        # 1. Staff gọi create_contract
        self.staff.create_contract(
            contract_id="C001",
            order_id="O001",
            customer_id="U001",
            vehicle_id="V001",
            start_date="2025-01-01",
            end_date="2025-01-06"
        )

        # 2. Kiểm tra file contracts.txt
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()

        self.assertEqual(len(lines), 1)

        data = lines[0].strip().split("|")
        self.assertEqual(data[0], "C001")        # contract_id
        self.assertEqual(data[1], "O001")        # order_id
        self.assertEqual(data[2], "U001")        # customer_id
        self.assertEqual(data[3], "S001")        # staff_id
        self.assertEqual(data[4], "V001")        # vehicle_id
        self.assertEqual(data[7], "active")      # status

    def tearDown(self):
        # Dọn file test
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            f.write("")

if __name__ == "__main__":
    unittest.main()
