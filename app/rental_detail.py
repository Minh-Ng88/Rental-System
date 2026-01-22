class RentalDetail:
    def __init__(self, detail_id, order_id, vehicle_id, price_per_day, days):
        self.detail_id = detail_id
        self.order_id = order_id
        self.vehicle_id = vehicle_id
        self.price_per_day = int(price_per_day)
        self.days = int(days)

    def calculate_sub_total(self):
        return self.price_per_day * self.days

    def save(self):
        with open("app/data/rental_details.txt", "a", encoding="utf-8") as f:
            f.write(
                f"{self.detail_id}|{self.order_id}|{self.vehicle_id}|"
                f"{self.price_per_day}|{self.days}\n"
            )
