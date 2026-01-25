from user import User
from datetime import datetime
from vehicle import Vehicle
from rental_order import RentalOrder
from rental_detail import RentalDetail

class Customer(User):
    def __init__(
        self,
        user_id: int,
        full_name: str,
        email: str,
        password: str,
        phone: str,
        address: str,
        created_at,
        role: str = "customer"
    ):
        super().__init__(
            user_id, full_name, email, password,
            phone, address, created_at, role
        )

    def _generate_order_id(self):
        try:
            with open("app/data/rental_orders.txt", "r", encoding="utf-8") as f:
                return "O" + str(len(f.readlines()) + 1).zfill(3)
        except FileNotFoundError:
            return "O001"

    def view_contracts(self):
        contracts = []
        with open("data/contracts.txt", "r", encoding="utf-8") as f:
            for line in f:
                data = line.strip().split("|")
                if data[2] == self.user_id:
                    contracts.append(line)
        return contracts

    def cancel_contract(self, contract_id):
        lines = []
        with open("data/contracts.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()

        with open("data/contracts.txt", "w", encoding="utf-8") as f:
            for line in lines:
                data = line.strip().split("|")
                if data[0] == contract_id and data[2] == self.user_id:
                    data[7] = "cancelled"
                    line = "|".join(data) + "\n"
                f.write(line)

    def rent_vehicle(self, vehicle_id, rental_date_str, return_date_str):
        # Validate date format
        try:
            rental_date = datetime.strptime(rental_date_str, "%Y-%m-%d")
            return_date = datetime.strptime(return_date_str, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format!")
            return None

        days = (return_date - rental_date).days
        if days <= 0:
            print("Return date must be AFTER rental date!")
            return None

        vehicle = Vehicle.find_by_id(vehicle_id)
        if not vehicle:
            print("Vehicle not found!")
            return None

        if not vehicle.is_available():
            print("Vehicle not available!")
            return None

        order_id = self._generate_order_id()
        total_price = int(vehicle.price_per_day) * days

        # Create order
        RentalOrder(
            order_id,
            self.user_id,
            rental_date_str,
            return_date_str,
            total_price,
            "new"
        ).save()

        # Create order detail
        RentalDetail(
            "D" + order_id,
            order_id,
            vehicle_id,
            vehicle.price_per_day,
            days
        ).save()

        # Update vehicle status
        vehicle.update_status("reserved")

        print("Rental order created successfully!")
        print(f"Order ID: {order_id}")
        print(f"Rental days: {days}")
        print(f"Total price: {total_price}")

        return order_id
