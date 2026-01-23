from admin import Admin
from staff import Staff
from customer import Customer
from vehicle import Vehicle
from rental_order import RentalOrder
from rental_detail import RentalDetail
from payment import Payment

def generate_order_id():
    try:
        with open("app/data/rental_orders.txt", "r", encoding="utf-8") as f:
            return "O" + str(len(f.readlines()) + 1).zfill(3)
    except FileNotFoundError:
        return "O001"

def customer_menu():
    print("\n--- CUSTOMER MENU ---")
    print("1. View vehicles")
    print("2. Create rental order")
    print("3. Make payment")
    print("0. Logout")


def staff_menu():
    print("\n--- STAFF MENU ---")
    print("1. Create contract")
    print("2. Vehicle handover")
    print("3. Vehicle return")
    print("0. Logout")


def admin_menu():
    print("\n--- ADMIN MENU ---")
    print("1. View all users")
    print("2. View all orders")
    print("3. View all contracts")
    print("4. View report")
    print("0. Logout")


def login():
    email = input("Email: ")
    password = input("Password: ")

    with open("app/data/users.txt", "r", encoding="utf-8") as f:
        for line in f:
            data = line.strip().split("|")
            if data[2] == email and data[3] == password:
                user_id, name, email, pwd, phone, addr, created, role = data

                if role == "admin":
                    return Admin(user_id, name, email, pwd, phone, addr, created)
                elif role == "staff":
                    return Staff(user_id, name, email, pwd, phone, addr, created)
                else:
                    return Customer(user_id, name, email, pwd, phone, addr, created)

    return None


def main():
    print("=== VEHICLE RENTAL SYSTEM ===")

    user = login()
    if not user:
        print("Login failed!")
        return

    print(f"Login success! Role: {user.role}")

    while True:

        # CUSTOMER
        if user.role == "customer":
            customer_menu()
            choice = input("Choose: ")

            if choice == "1":
                for v in Vehicle.load_all():
                    print(v.vehicle_id, v.name, v.price_per_day, v.status)

            elif choice == "2":
                print("\n--- CREATE RENTAL ORDER ---")

                # Auto order id
                order_id = generate_order_id()
                print(f"Generated Order ID: {order_id}")

                # Show date format
                print("Enter rental date (YYYY-MM-DD), example: 2025-01-10")
                rental_date = input("Rental date: ")

                print("Enter return date (YYYY-MM-DD), example: 2025-01-12")
                return_date = input("Return date: ")

                vehicle_id = input("Vehicle ID: ")
                days = int(input("Number of rental days: "))

                vehicle = Vehicle.find_by_id(vehicle_id)
                if not vehicle:
                    print("Vehicle not found!")
                    continue

                if not vehicle.is_available():
                    print("Vehicle is not available!")
                    continue

                total_price = int(vehicle.price_per_day) * days

                order = RentalOrder(
                    order_id,
                    user.user_id,
                    rental_date,
                    return_date,
                    total_price,
                    "new"
                )
                order.save()

                RentalDetail(
                    "D" + order_id,
                    order_id,
                    vehicle_id,
                    vehicle.price_per_day,
                    days
                    ).save()

                print("Rental order created successfully!")
                print(f"Total price: {total_price}")


        # STAFF
        elif user.role == "staff":
            staff_menu()
            choice = input("Choose: ")

            if choice == "1":
                staff = user
                staff.create_contract(
                    input("Contract ID: "),
                    input("Order ID: "),
                    input("Customer ID: "),
                    input("Vehicle ID: "),
                    "2025-01-10",
                    "2025-01-12"
                )

            elif choice == "2":
                user.handover_vehicle(input("Contract ID: "))
                print("Vehicle handed over")

            elif choice == "3":
                user.receive_vehicle(input("Contract ID: "))
                print("Vehicle returned")

            elif choice == "0":
                break

        # ADMIN
        elif user.role == "admin":
            admin_menu()
            choice = input("Choose: ")

            if choice == "1":
                print(user.view_all_users())

            elif choice == "2":
                print(user.view_all_orders())

            elif choice == "3":
                print(user.view_all_contracts())

            elif choice == "4":
                print(user.generate_report())

            elif choice == "0":
                break


if __name__ == "__main__":
    main()

