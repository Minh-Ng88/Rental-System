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
        with open("data/contracts.txt", "r", encoding="utf-8") as f:
            return f.readlines()

    def view_all_orders(self):
        with open("data/rental_orders.txt", "r", encoding="utf-8") as f:
            return f.readlines()

    def view_all_users(self):
        with open("data/users.txt", "r", encoding="utf-8") as f:
            return f.readlines()
