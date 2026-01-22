class RentalOrder:
    def __init__(self, order_id, user_id, rental_date, return_date, total_price, status):
        self.order_id = order_id
        self.user_id = user_id
        self.rental_date = rental_date
        self.return_date = return_date
        self.total_price = total_price
        self.status = status

    @staticmethod
    def load_all():
        orders = []
        with open("app/data/rental_orders.txt", "r", encoding="utf-8") as f:
            for line in f:
                orders.append(RentalOrder(*line.strip().split("|")))
        return orders

    def save(self):
        with open("app/data/rental_orders.txt", "a", encoding="utf-8") as f:
            f.write(
                f"{self.order_id}|{self.user_id}|{self.rental_date}|"
                f"{self.return_date}|{self.total_price}|{self.status}\n"
            )

    def update_status(self, new_status):
        orders = RentalOrder.load_all()
        with open("app/data/rental_orders.txt", "w", encoding="utf-8") as f:
            for o in orders:
                if o.order_id == self.order_id:
                    o.status = new_status
                f.write(
                    f"{o.order_id}|{o.user_id}|{o.rental_date}|"
                    f"{o.return_date}|{o.total_price}|{o.status}\n"
                )
    
    @staticmethod
    def find_by_user(user_id):
        return [o for o in RentalOrder.load_all() if o.user_id == user_id]

    def cancel(self):
        if self.status != "new":
            return False
        self.update_status("cancelled")
        return True