# test_vehicle_update_status.py

import unittest, sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from vehicle import Vehicle

DATA_FILE = "app/data/vehicles.txt"

class TestVehicleUpdateStatus(unittest.TestCase):

    def setUp(self):
        # Tạo thư mục và file dữ liệu test
        os.makedirs("app/data", exist_ok=True)

        # Ghi sẵn 1 vehicle vào file
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            f.write(
                "V011|Corolla|Toyota|5|available|100|Sedan Toyota\n"
            )

        # 1. Tạo Vehicle object (trùng vehicle_id trong file)
        self.vehicle = Vehicle(
            vehicle_id="V011",
            name="Corolla",
            brand="Toyota",
            capacity="5",
            status="available",
            price_per_day="100",
            description="Sedan Toyota"
        )

    def test_update_status(self):
        # 2. Gọi update_status("unavailable")
        self.vehicle.update_status("unavailable")

        # 3. Kiểm tra file vehicles.txt
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()

        self.assertEqual(len(lines), 1)

        data = lines[0].strip().split("|")
        self.assertEqual(data[0], "V011")             # vehicle_id
        self.assertEqual(data[4], "unavailable")      # status

    def tearDown(self):
        # Dọn file test
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            f.write("")

if __name__ == "__main__":
    unittest.main()
