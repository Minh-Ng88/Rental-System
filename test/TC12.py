# test_staff_handover_receive_vehicle.py

import unittest, sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from staff import Staff
from vehicle import Vehicle

CONTRACT_FILE = "app/data/contracts.txt"
VEHICLE_FILE = "app/data/vehicles.txt"

class TestStaffHandoverReceiveVehicle(unittest.TestCase):

    def setUp(self):
        # Tạo thư mục dữ liệu
        os.makedirs("app/data", exist_ok=True)

        # Tạo dữ liệu vehicle
        with open(VEHICLE_FILE, "w", encoding="utf-8") as f:
            f.write(
                "V001|Corolla|Toyota|5|reserved|100|Sedan Toyota\n"
            )

        # Tạo dữ liệu contract
        with open(CONTRACT_FILE, "w", encoding="utf-8") as f:
            f.write(
                "C01|O01|U01|S01|V001|2025-01-01|2025-01-06|active\n"
            )

        # Tạo Staff object
        self.staff = Staff(
            user_id="S01",
            full_name="Tran Van Staff",
            email="staff@gmail.com",
            password="123456",
            phone="0900000001",
            address="Staff Address",
            created_at="2025-01-01",
            role="staff"
        )

    def test_handover_and_receive_vehicle(self):
        # 1. Staff gọi handover_vehicle
        self.staff.handover_vehicle("C01")

        # Kiểm tra trạng thái xe sau handover
        vehicle = Vehicle.find_by_id("V001")
        self.assertEqual(vehicle.status, "rented")

        # 2. Staff gọi receive_vehicle
        self.staff.receive_vehicle("C01")

        # 3. Kiểm tra contract status
        with open(CONTRACT_FILE, "r", encoding="utf-8") as f:
            line = f.readline().strip()

        data = line.split("|")
        self.assertEqual(data[0], "C01")            # contract_id
        self.assertEqual(data[7], "completed")      # status

    def tearDown(self):
        # Dọn file test
        with open(CONTRACT_FILE, "w", encoding="utf-8") as f:
            f.write("")
        with open(VEHICLE_FILE, "w", encoding="utf-8") as f:
            f.write("")

if __name__ == "__main__":
    unittest.main()
