from user import User

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
