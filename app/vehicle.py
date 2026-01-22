class Vehicle:
    def __init__(self, vehicle_id, name, brand, capacity, status, price_per_day, description):
        self.vehicle_id = vehicle_id
        self.name = name
        self.brand = brand
        self.capacity = capacity
        self.status = status
        self.price_per_day = price_per_day
        self.description = description

    @staticmethod
    def load_all():
        vehicles = []
        with open("app/data/vehicles.txt", "r", encoding="utf-8") as f:
            for line in f:
                vehicles.append(Vehicle(*line.strip().split("|")))
        return vehicles

    @staticmethod
    def find_by_id(vehicle_id):
        for v in Vehicle.load_all():
            if v.vehicle_id == vehicle_id:
                return v
        return None

    def save(self):
        with open("app/data/vehicles.txt", "a", encoding="utf-8") as f:
            f.write(
                f"{self.vehicle_id}|{self.name}|{self.brand}|{self.capacity}|"
                f"{self.status}|{self.price_per_day}|{self.description}\n"
            )

    def update_status(self, new_status):
        vehicles = Vehicle.load_all()
        with open("app/data/vehicles.txt", "w", encoding="utf-8") as f:
            for v in vehicles:
                if v.vehicle_id == self.vehicle_id:
                    v.status = new_status
                f.write(
                    f"{v.vehicle_id}|{v.name}|{v.brand}|{v.capacity}|"
                    f"{v.status}|{v.price_per_day}|{v.description}\n"
                )

    @staticmethod
    def search(keyword):
        result = []
        for v in Vehicle.load_all():
            if keyword.lower() in v.name.lower() or keyword.lower() in v.description.lower():
                result.append(v)
        return result

    def is_available(self):
        return self.status == "available"