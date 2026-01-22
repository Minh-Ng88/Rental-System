class User:
    def __init__(self, user_id, full_name, email, password, phone, address, created_at, role):
        self.user_id = user_id
        self.full_name = full_name
        self.email = email
        self.password = password
        self.phone = phone
        self.address = address
        self.created_at = created_at
        self.role = role

    @staticmethod
    def load_all():
        users = []
        with open("app/data/users.txt", "r", encoding="utf-8") as f:
            for line in f:
                data = line.strip().split("|")
                users.append(User(*data))
        return users

    @staticmethod
    def login(email, password):
        with open("app/data/users.txt", "r", encoding="utf-8") as f:
            for line in f:
                user_id, name, mail, pwd, *_ = line.strip().split("|")
                if mail == email and pwd == password:
                    return True
        return False

    def save(self):
        with open("app/data/users.txt", "a", encoding="utf-8") as f:
            f.write(
                f"{self.user_id}|{self.full_name}|{self.email}|{self.password}|"
                f"{self.phone}|{self.address}|{self.created_at}|{self.role}\n"
            )

    def update_profile(self, phone, address):
        users = User.load_all()
        with open("data/users.txt", "w", encoding="utf-8") as f:
            for u in users:
                if u.user_id == self.user_id:
                    u.phone = phone
                    u.address = address
                f.write(
                    f"{u.user_id}|{u.full_name}|{u.email}|{u.password}|"
                    f"{u.phone}|{u.address}|{u.created_at}|{u.role}\n"
                )
    
    def change_password(self, new_password):
        users = User.load_all()
        with open("app/data/users.txt", "w", encoding="utf-8") as f:
            for u in users:
                if u.user_id == self.user_id:
                    u.password = new_password
                f.write(
                    f"{u.user_id}|{u.full_name}|{u.email}|{u.password}|"
                    f"{u.phone}|{u.address}|{u.created_at}|{u.role}\n"
                )
