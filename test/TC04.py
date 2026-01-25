# test_vehicle_is_available.py

import unittest, sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from vehicle import Vehicle

class TestVehicleIsAvailable(unittest.TestCase):

    def test_vehicle_available(self):
        # 1. Create vehicle object (status = available)
        vehicle = Vehicle(
            vehicle_id="V100",
            name="Corolla",
            brand="Toyota",
            capacity="5",
            status="available",
            price_per_day="100",
            description="Toyota Sedan"
        )

        # 2. Gọi is_available()
        result = vehicle.is_available()

        self.assertTrue(result)

    def test_vehicle_not_available(self):
        # Test thêm: xe không available
        vehicle = Vehicle(
            vehicle_id="V101",
            name="Fortuner",
            brand="Toyota",
            capacity="7",
            status="rented",
            price_per_day="150",
            description="SUV Toyota"
        )

        result = vehicle.is_available()

        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()
