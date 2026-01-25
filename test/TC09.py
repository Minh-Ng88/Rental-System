# test_user_login.py

import unittest, sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from user import User

DATA_FILE = "app/data/users.txt"

class TestUserLogin(unittest.TestCase):

    def setUp(self):
        # Tạo thư mục và file dữ liệu test
        os.makedirs("app/data", exist_ok=True)

        with open(DATA_FILE, "w", encoding="utf-8") as f:
            f.write(
                "U001|Nguyen Van A|a@gmail.com|123456|0900000001|Address A|2025-01-01|customer\n"
                "U002|Nguyen Van B|b@gmail.com|abcdef|0900000002|Address B|2025-01-01|staff\n"
            )

    def test_login_success(self):
        # 1–2. Login với thông tin đúng
        result = User.login("a@gmail.com", "123456")
        self.assertTrue(result)

    def test_login_wrong_password(self):
        # 3. Sai mật khẩu
        result = User.login("a@gmail.com", "wrongpass")
        self.assertFalse(result)

    def test_login_wrong_email(self):
        # 3. Sai email
        result = User.login("wrong@gmail.com", "123456")
        self.assertFalse(result)

    def tearDown(self):
        # Dọn file test
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            f.write("")

if __name__ == "__main__":
    unittest.main()
