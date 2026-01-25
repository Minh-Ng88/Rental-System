# test_rental_detail.py

import unittest, sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from rental_detail import RentalDetail

class TestRentalDetail(unittest.TestCase):

    def test_calculate_sub_total(self):
        # 1. Tạo rental detail với price_per_day = 100
        rental_detail = RentalDetail(
            detail_id="D001",
            order_id="O001",
            vehicle_id="V001",
            price_per_day=100,
            days=5  # 2. Booking 5 ngày
        )

        # 3. Gọi calculate_sub_total()
        sub_total = rental_detail.calculate_sub_total()

        # Kiểm tra kết quả
        self.assertEqual(sub_total, 500)

if __name__ == "__main__":
    unittest.main()
