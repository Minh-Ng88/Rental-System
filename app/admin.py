from user import User

class Admin(User):
    def __init__(
        self,
        user_id: int,
        full_name: str,
        email: str,
        password: str,
        phone: str,
        address: str,
        created_at,
        role: str = "admin"
    ):
        super().__init__(
            user_id, full_name, email, password,
            phone, address, created_at, role
        )
        
    def view_all_contracts(self):
        with open("app/data/contracts.txt", "r", encoding="utf-8") as f:
            return f.readlines()

    def view_all_orders(self):
        with open("app/data/rental_orders.txt", "r", encoding="utf-8") as f:
            return f.readlines()

    def view_all_users(self):
        with open("app/data/users.txt", "r", encoding="utf-8") as f:
            return f.readlines()
        
    def add_vehicle(self, vehicle):
        vehicle.save()

    def remove_vehicle(self, vehicle_id):
        vehicles = []
        with open("app/data/vehicles.txt", "r", encoding="utf-8") as f:
            vehicles = f.readlines()

        with open("app/data/vehicles.txt", "w", encoding="utf-8") as f:
            for line in vehicles:
                if not line.startswith(vehicle_id):
                    f.write(line)

    def generate_report(self):
        orders = open("app/data/rental_orders.txt", "r", encoding="utf-8").readlines()
        payments = open("app/data/payments.txt", "r", encoding="utf-8").readlines()
        return {
            "total_orders": len(orders),
            "total_payments": len(payments)
        }
