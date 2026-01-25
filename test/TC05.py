# test_user_update_profile.py

import unittest, sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from user import User

DATA_FILE = "app/data/users.txt"

class TestUserUpdateProfile(unittest.TestCase):

    def setUp(self):
        # Tạo thư mục và file dữ liệu test
        os.makedirs("app/data", exist_ok=True)

        with open(DATA_FILE, "w", encoding="utf-8") as f:
            f.write(
                "U001|Nguyen Van A|a@gmail.com|123456|0123456789|Old Address|2025-01-01|customer\n"
            )

        # 1. Tạo User object
        self.user = User(
            user_id="U001",
            full_name="Nguyen Van A",
            email="a@gmail.com",
            password="123456",
            phone="0123456789",
            address="Old Address",
            created_at="2025-01-01",
            role="customer"
        )

    def test_update_profile(self):
        # 2. Gọi update_profile
        self.user.update_profile("0900000099", "New Address")

        # 3. Kiểm tra file users.txt
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            line = f.readline().strip()

        data = line.split("|")
        self.assertEqual(data[4], "0900000099")   # phone
        self.assertEqual(data[5], "New Address")  # address

    def tearDown(self):
        # Dọn file test
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            f.write("")

if __name__ == "__main__":
    unittest.main()
