# test_vehicle_search.py

import unittest, sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from vehicle import Vehicle

DATA_FILE = "app/data/vehicles.txt"

class TestVehicleSearch(unittest.TestCase):

    def setUp(self):
        # Tạo thư mục và file dữ liệu test
        os.makedirs("app/data", exist_ok=True)

        with open(DATA_FILE, "w", encoding="utf-8") as f:
            f.write(
                "V001|Camry|Toyota|5|available|100|Sedan Toyota\n"
                "V002|Vios|Toyota|5|available|90|Compact Toyota\n"
                "V003|Civic|Honda|5|available|95|Sedan Honda\n"
            )

    def test_search_toyota(self):
        # 1. Gọi Vehicle.search("Toyota")
        results = Vehicle.search("Toyota")

        # 2. Đếm kết quả
        self.assertEqual(len(results), 2)

    def tearDown(self):
        # Dọn file sau khi test
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            f.write("")

if __name__ == "__main__":
    unittest.main()
