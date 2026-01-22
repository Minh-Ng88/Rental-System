class Payment:
    def __init__(self, payment_id, order_id, method, payment_date, status):
        self.payment_id = payment_id
        self.order_id = order_id
        self.method = method
        self.payment_date = payment_date
        self.status = status

    def save(self):
        with open("app/data/payments.txt", "a", encoding="utf-8") as f:
            f.write(
                f"{self.payment_id}|{self.order_id}|{self.method}|"
                f"{self.payment_date}|{self.status}\n"
            )

    def verify_payment(self):
        return self.status == "paid"
    
    def is_paid(order_id):
        with open("app/data/payments.txt", "r", encoding="utf-8") as f:
            for line in f:
                _, o_id, _, _, status = line.strip().split("|")
                if o_id == order_id and status == "paid":
                    return True
        return False
