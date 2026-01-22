from user import User

class Staff(User):
    def __init__(
        self,
        user_id: int,
        full_name: str,
        email: str,
        password: str,
        phone: str,
        address: str,
        created_at,
        role: str = "staff"
    ):
        super().__init__(
            user_id, full_name, email, password,
            phone, address, created_at, role
        )
        
    def create_contract(
        self, contract_id, order_id, customer_id,
        vehicle_id, start_date, end_date
    ):
        with open("app/data/contracts.txt", "a", encoding="utf-8") as f:
            f.write(
                f"{contract_id}|{order_id}|{customer_id}|{self.user_id}|"
                f"{vehicle_id}|{start_date}|{end_date}|active\n"
            )

    def handover_vehicle(self, contract_id):
        self._update_contract_status(contract_id, "in_use")

    def receive_vehicle(self, contract_id):
        self._update_contract_status(contract_id, "completed")

    def print_contract(self, contract_id):
        with open("app/data/contracts.txt", "r", encoding="utf-8") as f:
            for line in f:
                if line.startswith(contract_id):
                    print("\n--- RENTAL CONTRACT ---")
                    print(line)
                    print("----------------------")

    def _update_contract_status(self, contract_id, new_status):
        lines = []
        with open("app/data/contracts.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()

        with open("app/data/contracts.txt", "w", encoding="utf-8") as f:
            for line in lines:
                data = line.strip().split("|")
                if data[0] == contract_id:
                    data[7] = new_status
                    line = "|".join(data) + "\n"
                f.write(line)

    def record_damage(self, contract_id, description, cost):
        with open("app/data/damages.txt", "a", encoding="utf-8") as f:
            f.write(f"{contract_id}|{description}|{cost}\n")